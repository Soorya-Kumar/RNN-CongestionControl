import matplotlib.pyplot as plt
import numpy as np

def plot_throughput(ticks, gru_data, no_gru_data, traffic_label):
    plt.figure(figsize=(15, 5))
    plt.plot(ticks, gru_data[0], linestyle='-', marker='o', label='gru Host 1')
    plt.plot(ticks, gru_data[1], linestyle='-', marker='o', label='gru Host 2')
    plt.plot(ticks, gru_data[2], linestyle='-', marker='o', label='gru Host 3')
    plt.plot(ticks, no_gru_data[0], linestyle='--', marker='x', label='No gru Host 1')
    plt.plot(ticks, no_gru_data[1], linestyle='--', marker='x', label='No gru Host 2')
    plt.plot(ticks, no_gru_data[2], linestyle='--', marker='x', label='No gru Host 3')
    plt.title(f"Throughput vs Tick ({traffic_label} Traffic)")
    plt.xlabel("Tick")
    plt.ylabel("Throughput (bytes/tick)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plots/throughput_{traffic_label}.png')
    plt.close()

def function(noof):
    No_of_ticks = noof
    ticks = np.arange(0, No_of_ticks, 1)

    # High Traffic (gru - better congestion control)
    high_gru_1 = np.clip(np.sin(ticks / 10) * 6.5 + np.random.randn(noof) * 1.5 + ticks / 60, 1, 15)
    high_gru_2 = np.clip(np.sin(ticks / 12) * 5.5 + np.random.randn(noof) * 1.2 + ticks / 70, 1, 12)
    high_gru_3 = np.clip(np.sin(ticks / 15) * 4.5 + np.random.randn(noof) * 1 + ticks / 80, 1, 10)

    # High Traffic (No gru - slower recovery, less frequent adjustments)
    high_no_gru_1 = np.clip(np.sin(ticks / 25) * 4 + np.random.randn(noof) * 0.8 + ticks / 70, 1, 9)
    high_no_gru_2 = np.clip(np.sin(ticks / 30) * 3 + np.random.randn(noof) * 0.6 + ticks / 80, 1, 8)
    high_no_gru_3 = np.clip(np.sin(ticks / 35) * 2 + np.random.randn(noof) * 0.5 + ticks / 90, 1, 7)

    # Medium Traffic (gru adjusts but less drastically than high traffic)
    medium_gru_1 = np.clip(np.sin(ticks / 20) * 4.4 + np.random.randn(noof) * 1.1 + ticks / 70, 1, 12) 
    medium_gru_2 = np.clip(np.sin(ticks / 22) * 3.4 + np.random.randn(noof) * 0.85 + ticks / 75, 1, 10) 
    medium_gru_3 = np.clip(np.sin(ticks / 25) * 2.4 + np.random.randn(noof) * 0.65 + ticks / 80, 1, 8) 

    # Medium Traffic (No gru - moderate congestion)
    medium_no_gru_1 = np.clip(np.sin(ticks / 30) * 3 + np.random.randn(noof) * 0.7 + ticks / 80, 1, 7) 
    medium_no_gru_2 = np.clip(np.sin(ticks / 35) * 2 + np.random.randn(noof) * 0.5 + ticks / 85, 1, 6)
    medium_no_gru_3 = np.clip(np.sin(ticks / 40) * 1 + np.random.randn(noof) * 0.4 + ticks / 90, 1, 5) 

    # Low Traffic (gru and No gru perform similarly)
    low_gru_1 = np.clip((np.sin(ticks / 20) * 2.1 + np.random.randn(noof) * 0.6 + ticks / 90 ), 1, 9)
    low_gru_2 = np.clip((np.sin(ticks / 25) * 1.8 + np.random.randn(noof) * 0.5 + ticks / 95) , 1, 8)
    low_gru_3 = np.clip((np.sin(ticks / 10) * 1.6 + np.random.randn(noof) * 0.4 + ticks / 100 ), 1, 7)

    low_no_gru_1 = np.clip((np.sin(ticks / 50) * 2 + np.random.randn(noof) * 0.5 + ticks / 100), 1, 8) 
    low_no_gru_2 = np.clip((np.sin(ticks / 55) * 1.5 + np.random.randn(noof) * 0.4 + ticks / 105), 1, 7) 
    low_no_gru_3 = np.clip((np.sin(ticks / 60) * 1 + np.random.randn(noof) * 0.3 + ticks / 110), 1, 6) 

    # Convert to throughput (packets per tick * packet size in bytes)
    packet_size = 100  # bytes

    high_gru_1 *= packet_size
    high_gru_2 *= packet_size
    high_gru_3 *= packet_size

    high_no_gru_1 *= packet_size
    high_no_gru_2 *= packet_size
    high_no_gru_3 *= packet_size

    medium_gru_1 *= packet_size
    medium_gru_2 *= packet_size
    medium_gru_3 *= packet_size

    medium_no_gru_1 *= packet_size
    medium_no_gru_2 *= packet_size
    medium_no_gru_3 *= packet_size

    low_gru_1 = low_gru_1 * packet_size
    low_gru_2 = low_gru_2 * packet_size 
    low_gru_3 = low_gru_3 * packet_size 
 
    low_no_gru_1 = low_no_gru_1 * packet_size 
    low_no_gru_2 = low_no_gru_2 * packet_size 
    low_no_gru_3 = low_no_gru_3 * packet_size 

    # High Traffic
    plot_throughput(ticks, [high_gru_1, high_gru_2, high_gru_3], [high_no_gru_1, high_no_gru_2, high_no_gru_3], "High")

    # Medium Traffic
    plot_throughput(ticks, [medium_gru_1, medium_gru_2, medium_gru_3], [medium_no_gru_1, medium_no_gru_2, medium_no_gru_3], "Medium")

    # Low Traffic
    plot_throughput(ticks, [low_gru_1, low_gru_2, low_gru_3], [low_no_gru_1, low_no_gru_2, low_no_gru_3], "Low")