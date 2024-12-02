# Reimport necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# Define the ticks again
ticks = np.arange(0, 500, 1)


def graph_delay(noofticks, delay_high_lstm_, delay_high_normal_, delay_medium_lstm_, delay_medium_normal_, delay_low_lstm_, delay_low_normal_):
    fig, axs = plt.subplots(3, 1, figsize=(14, 14))
    # High traffic plot
    axs[0].plot(ticks, delay_high_lstm_, label="High Traffic LSTM", color="blue")
    axs[0].plot(ticks, delay_high_normal_, label="High Traffic Normal", color="orange")
    axs[0].set_title("Delay vs Tick - High Traffic ()")
    axs[0].set_xlabel("Tick")
    axs[0].set_ylabel("Delay (ticks)")
    axs[0].legend()
    # Medium traffic plot
    axs[1].plot(ticks, delay_medium_lstm_, label="Medium Traffic LSTM", color="green")
    axs[1].plot(ticks, delay_medium_normal_, label="Medium Traffic Normal", color="red")
    axs[1].set_title("Delay vs Tick - Medium Traffic ()")
    axs[1].set_xlabel("Tick")
    axs[1].set_ylabel("Delay (ticks)")
    axs[1].legend()
    # Low traffic plot
    axs[2].plot(ticks, delay_low_lstm_, label="Low Traffic LSTM", color="purple")
    axs[2].plot(ticks, delay_low_normal_, label="Low Traffic Normal", color="brown")
    axs[2].set_title("Delay vs Tick - Low Traffic ()")
    axs[2].set_xlabel("Tick")
    axs[2].set_ylabel("Delay (ticks)")
    axs[2].legend()

    plt.tight_layout()
    plt.savefig(f'plots/delay.png')
    plt.close()
    



def plot_throughput(ticks, lstm_data, no_lstm_data, traffic_label):
    plt.figure(figsize=(15, 5))
    plt.plot(ticks, lstm_data[0], linestyle='-', marker='o', label='LSTM Host 1')
    plt.plot(ticks, lstm_data[1], linestyle='-', marker='o', label='LSTM Host 2')
    plt.plot(ticks, lstm_data[2], linestyle='-', marker='o', label='LSTM Host 3')
    plt.plot(ticks, no_lstm_data[0], linestyle='--', marker='x', label='No LSTM Host 1')
    plt.plot(ticks, no_lstm_data[1], linestyle='--', marker='x', label='No LSTM Host 2')
    plt.plot(ticks, no_lstm_data[2], linestyle='--', marker='x', label='No LSTM Host 3')
    plt.title(f"Throughput vs Tick ({traffic_label} Traffic)")
    plt.xlabel("Tick")
    plt.ylabel("Throughput (bytes/tick)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plots/throughput_{traffic_label}.png')
    plt.close()

def throughput_graph(noofticks, throughput_data_high, throughput_data_medium, throughput_data_low, throughput_data_high_no, throughput_data_medium_no, throughput_data_low_no):
    high_lstm_1 = [x[0] for x in throughput_data_high]
    high_lstm_2 = [x[1] for x in throughput_data_high]
    high_lstm_3 = [x[2] for x in throughput_data_high]
    
    medium_lstm_1 = [x[0] for x in throughput_data_medium]
    medium_lstm_2 = [x[1] for x in throughput_data_medium]
    medium_lstm_3 = [x[2] for x in throughput_data_medium] 
    
    low_lstm_1 = [x[0] for x in throughput_data_low]
    low_lstm_2 = [x[1] for x in throughput_data_low]
    low_lstm_3 = [x[2] for x in throughput_data_low]
    
    high_no_lstm_1 = [x[0] for x in throughput_data_high_no]
    high_no_lstm_2 = [x[1] for x in throughput_data_high_no]
    high_no_lstm_3 = [x[2] for x in throughput_data_high_no]
    
    medium_no_lstm_1 = [x[0] for x in throughput_data_medium_no]
    medium_no_lstm_2 = [x[1] for x in throughput_data_medium_no]
    medium_no_lstm_3 = [x[2] for x in throughput_data_medium_no]
    
    low_no_lstm_1 = [x[0] for x in throughput_data_low_no]
    low_no_lstm_2 = [x[1] for x in throughput_data_low_no]
    low_no_lstm_3 = [x[2] for x in throughput_data_low_no]

    plot_throughput(ticks, [high_lstm_1, high_lstm_2, high_lstm_3], [high_no_lstm_1, high_no_lstm_2, high_no_lstm_3], "High")
    plot_throughput(ticks, [medium_lstm_1, medium_lstm_2, medium_lstm_3], [medium_no_lstm_1, medium_no_lstm_2, medium_no_lstm_3], "Medium")
    plot_throughput(ticks, [low_lstm_1, low_lstm_2, low_lstm_3], [low_no_lstm_1, low_no_lstm_2, low_no_lstm_3], "Low")







def plot_traffic_scenario(lstm1, lstm2, lstm3, no_lstm1, no_lstm2, no_lstm3, title, type):
    plt.figure(figsize=(18, 6))
    plt.plot(ticks, lstm1, label='host1 (LSTM)', color='blue')
    plt.plot(ticks, lstm2, label='host2 (LSTM)', color='orange')
    plt.plot(ticks, lstm3, label='host3 (LSTM)', color='green')
    plt.plot(ticks, no_lstm1, label='host1 (No LSTM)', linestyle='--', color='blue')
    plt.plot(ticks, no_lstm2, label='host2 (No LSTM)', linestyle='--', color='orange')
    plt.plot(ticks, no_lstm3, label='host3 (No LSTM)', linestyle='--', color='green')
    plt.title(title)
    plt.xlabel('tick')
    plt.ylabel('window_size')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plots/winsize_{type}.png')
    plt.close()


def winsize_plot(noofticks, window_data_high, window_data_medium, window_data_low, window_data_high_no, window_data_medium_no, window_data_low_no):
   
    high_lstm_1 = [x[0] for x in window_data_high]
    high_lstm_2 = [x[1] for x in window_data_high]
    high_lstm_3 = [x[2] for x in window_data_high]

    medium_lstm_1 = [x[0] for x in window_data_medium]
    medium_lstm_2 = [x[1] for x in window_data_medium]
    medium_lstm_3 = [x[2] for x in window_data_medium]

    low_lstm_1 = [x[0] for x in window_data_low]
    low_lstm_2 = [x[1] for x in window_data_low]
    low_lstm_3 = [x[2] for x in window_data_low]

    high_no_lstm_1 = [x[0] for x in window_data_high_no]
    high_no_lstm_2 = [x[1] for x in window_data_high_no]
    high_no_lstm_3 = [x[2] for x in window_data_high_no]

    medium_no_lstm_1 = [x[0] for x in window_data_medium_no]
    medium_no_lstm_2 = [x[1] for x in window_data_medium_no]
    medium_no_lstm_3 = [x[2] for x in window_data_medium_no]

    low_no_lstm_1 = [x[0] for x in window_data_low_no]
    low_no_lstm_2 = [x[1] for x in window_data_low_no]
    low_no_lstm_3 = [x[2] for x in window_data_low_no]

    
    plot_traffic_scenario(high_lstm_1, high_lstm_2, high_lstm_3, high_no_lstm_1, high_no_lstm_2, high_no_lstm_3, 'High Traffic Scenario (Frequent Adjustments due to LSTM)', 'HighTraffic')
    plot_traffic_scenario(medium_lstm_1, medium_lstm_2, medium_lstm_3, medium_no_lstm_1, medium_no_lstm_2, medium_no_lstm_3, 'Medium Traffic Scenario (Moderate Adjustments)', 'MediumTraffic')
    plot_traffic_scenario(low_lstm_1, low_lstm_2, low_lstm_3, low_no_lstm_1, low_no_lstm_2, low_no_lstm_3, 'Low Traffic Scenario (Minimal Adjustments)', 'LowTraffic')

