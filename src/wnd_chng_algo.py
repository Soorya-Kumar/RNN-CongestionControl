import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, RepeatVector, TimeDistributed, Dense

def scale_data(data, mean, std):
    return (data - mean) / std

def unscale_data(data, mean, std):
    return (data * std) + mean

# Define the model
look_back = 50
look_ahead = 20
neuron1 = 70
neuron2 = 70
neuron3 = 70

series_mean = 11696639.313548004 
series_std =  4915670.188839178

model = Sequential()
model.add(LSTM(neuron1, input_shape=(look_back, 1)))
model.add(RepeatVector(look_ahead))
model.add(LSTM(neuron2, return_sequences=True))
model.add(LSTM(neuron3, return_sequences=True))
model.add(LSTM(neuron1, return_sequences=True))
model.add(LSTM(neuron1, return_sequences=True))
model.add(TimeDistributed(Dense(1)))

model.compile(loss="mse", optimizer="rmsprop", metrics=["mape"])
model.load_weights('model.weights.h5')


# Function to predict throughput and calculate a single congestion control output
def predict_throughput_and_control(throughput_data):

    throughput_data = scale_data(throughput_data, series_mean, series_std).reshape(1, look_back, 1)
    predicted_throughput = model.predict(throughput_data).flatten()
    predicted_throughput = unscale_data(predicted_throughput, series_mean, series_std)
    
    ## By analyzing the rate of change,
    #  we can infer whether the throughput is increasing, decreasing,
    #  or remaining stable over time.
    # FIRST STATISTICAL PRINCIPLE
    rate_of_change = np.diff(predicted_throughput)
    
    
    ## A positive average rate indicates an increasing 
    # trend, while a negative average rate indicates a decreasing trend
    avg_rate_of_change = np.mean(rate_of_change)
    
    
    max_rate = np.max(np.abs(rate_of_change))  # Use the max absolute change to normalize
    
    ## if close to -1 then it is strongly decreasing
    ## if close to 1 then it is strongly increasing
    # if close to 0 then it is stable

    if max_rate != 0:
        normalized_control_output = avg_rate_of_change / max_rate
    else:
        normalized_control_output = 0 
       
    return predicted_throughput, normalized_control_output


def model_calling(throughput_data):
    predicted_throughput, control_output = predict_throughput_and_control(throughput_data)
    return control_output 
