
#%%
import math
import numpy as np
from glob import glob

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.svm import SVR
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, GRU
from tensorflow.keras.metrics import MeanAbsoluteError
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import SGD, Adam, RMSprop, Adagrad
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.metrics import MeanAbsolutePercentageError as MAPE

#%%

def read_data (path = 'dataset_and_preprocess/fdata_throughput'):
    with open(path) as f:
        lines = f.read().splitlines()
    series = np.array(list(map(int, lines)))
    return series

def train_test_split(dataset, train_frac):
    train_size = int(len(dataset)*train_frac)
    return dataset[:train_size], dataset[train_size:]

def create_datasets(dataset, look_back=1, look_ahead=1):
    data_x, data_y = [], []
    for i in range(len(dataset)-look_back-look_ahead+1):
        window = dataset[i:(i+look_back)]
        data_x.append(window)
        data_y.append(dataset[i + look_back:i + look_back + look_ahead])
    return np.array(data_x), np.array(data_y)

def plot_series(time, series, format="-", start=0, end=None, figsize=(10,6), xlabel="Time", ylabel="Paclets per Second", path="test.png"):
    fig = plt.figure(1, figsize)
    plt.plot(time[start:end], series[start:end], format)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
    # plt.savefig(path)
    # plt.close()


def plot_hist(data, bins = 20 , xlabel = "" , ylabel = "" , title = "", path="test1.png"):
    plt.hist(data, bins, color = 'green',edgecolor = 'black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.show()
    plt.savefig(path)
    plt.close()

def reverse_scale(data, mean, std):
    for x in np.nditer(data, op_flags=['readwrite']):
        x[...] = x*std + mean
    return data

def calculate_error(train_y, test_y, pred_train, pred_test):
    test_score = math.sqrt(mean_squared_error(test_y, pred_test))
    train_score = math.sqrt(mean_squared_error(train_y, pred_train))
    return train_score, test_score

def mean_absolute_percentage(y, y_pred):
    return np.mean(np.abs((y - y_pred) / y)) * 100


def plot_1_error(pred_test, test_y, er1, path="test.png"):
    fig = plt.figure(1, (18, 13))
    test_y  = test_y.reshape(len(test_y))
    pred_test = pred_test.reshape(len(pred_test))
    plt.plot(test_y, label="Observed")
    plt.plot(pred_test, color="red", label="Predicted, MAPE: " + str(round(er1, 5)) + "%")
    plt.title("1 step ahead prediction")
    plt.ylabel("Number of Packets / minute")
    plt.legend(loc=1, fontsize=8, framealpha=0.8)
    plt.savefig(path)
    plt.close()

def plot_4_errors(pred_test, test_y, er1, er2, er3, er4, path="test.png"):
    fig = plt.figure(1, (18, 13))
    plt.subplot(221)
    plt.plot(test_y[:, 0, :], label="Observed")
    plt.plot(pred_test[:, 0, :], color="red", label="Predicted, MAPE: " + str(round(er1, 5)) + "%")
    plt.title("1 step ahead prediction")
    plt.ylabel("Number of Packets / minute")
    plt.legend(loc=1, fontsize=8, framealpha=0.8)

    plt.subplot(222)
    plt.plot(pred_test[:, 3, :], color="red", label="Predicted, MAPE: " + str(round(er2, 5)) + "%")
    plt.plot(test_y[:, 3, :], label="Observed")
    plt.title("4 step ahead prediction")
    plt.legend(loc=1, fontsize=8, framealpha=0.8)

    plt.subplot(223)
    plt.plot(pred_test[:, 7, :], color="red", label="Predicted, MAPE: " + str(round(er3, 5)) + "%")
    plt.plot(test_y[:, 7, :], label="Observed")
    plt.title("8 step ahead prediction")
    plt.legend(loc=1, fontsize=8, framealpha=0.8)

    plt.subplot(224)
    plt.plot(pred_test[:, 15, :], color="red", label="Predicted, MAPE: " + str(round(er4, 5)) + "%")
    plt.plot(test_y[:, 15, :], label="Observed")
    plt.title("16 step ahead prediction")
    plt.legend(loc=1, fontsize=8, framealpha=0.8)

    # plt.show()
    plt.savefig(path)
    plt.close()