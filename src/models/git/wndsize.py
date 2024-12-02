# Adjusting the simulation based on the updated understanding of the traffic behavior
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_traffic_scenario(ticks, gru1, gru2, gru3, no_gru1, no_gru2, no_gru3, title, type):
    plt.figure(figsize=(18, 6))
    plt.plot(ticks, gru1, label='host1 (gru)', color='blue')
    plt.plot(ticks, gru2, label='host2 (gru)', color='orange')
    plt.plot(ticks, gru3, label='host3 (gru)', color='green')
    plt.plot(ticks, no_gru1, label='host1 (No gru)', linestyle='--', color='blue')
    plt.plot(ticks, no_gru2, label='host2 (No gru)', linestyle='--', color='orange')
    plt.plot(ticks, no_gru3, label='host3 (No gru)', linestyle='--', color='green')
    plt.title(title)
    plt.xlabel('tick')
    plt.ylabel('window_size')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plots/winsize_{type}.png')
    plt.close()

def function(noof):
    No_of_ticks = noof
    ticks = np.arange(0, No_of_ticks, 1)

    high_gru_1 = np.clip(np.sin(ticks / 10) * 6.5 + np.random.randn(noof) * 1.5 + ticks / 60, 1, 15).astype(int)
    high_gru_2 = np.clip(np.sin(ticks / 12) * 5.5 + np.random.randn(noof) * 1.2 + ticks / 70, 1, 12).astype(int)
    high_gru_3 = np.clip(np.sin(ticks / 15) * 4.5 + np.random.randn(noof) * 1 + ticks / 80, 1, 10).astype(int)
    
    high_no_gru_1 = np.clip(np.sin(ticks / 25) * 4 + np.random.randn(noof) * 0.8 + ticks / 70, 1, 9).astype(int)
    high_no_gru_2 = np.clip(np.sin(ticks / 30) * 3 + np.random.randn(noof) * 0.6 + ticks / 80, 1, 8).astype(int)
    high_no_gru_3 = np.clip(np.sin(ticks / 35) * 2 + np.random.randn(noof) * 0.5 + ticks / 90, 1, 7).astype(int)
    
    medium_gru_1 = np.clip(np.sin(ticks / 20) * 4.4 + np.random.randn(noof) * 1.1 + ticks / 70, 1, 12).astype(int) 
    medium_gru_2 = np.clip(np.sin(ticks / 22) * 3.4 + np.random.randn(noof) * 0.85 + ticks / 75, 1, 10).astype(int) 
    medium_gru_3 = np.clip(np.sin(ticks / 25) * 2.4 + np.random.randn(noof) * 0.65 + ticks / 80, 1, 8).astype(int) 
    
    medium_no_gru_1 = np.clip(np.sin(ticks / 30) * 3 + np.random.randn(noof) * 0.7 + ticks / 80, 1, 7).astype(int) 
    medium_no_gru_2 = np.clip(np.sin(ticks / 35) * 2 + np.random.randn(noof) * 0.5 + ticks / 85, 1, 6).astype(int) 
    medium_no_gru_3 = np.clip(np.sin(ticks / 40) * 1 + np.random.randn(noof) * 0.4 + ticks / 90, 1, 5).astype(int) 
    
    low_gru_1 = np.clip((np.sin(ticks / 20) * 2.6 + np.random.randn(noof) * 0.4 + ticks / 90), 1, 8).astype(int) 
    low_gru_2 = np.clip((np.sin(ticks / 25) * 2.1 + np.random.randn(noof) * 0.3 + ticks / 95), 1, 7).astype(int) 
    low_gru_3 = np.clip((np.sin(ticks / 10) * 1.6 + np.random.randn(noof) * 0.2 + ticks / 100), 1, 6).astype(int) 
    
    low_no_gru_1 = np.clip((np.sin(ticks / 50) * 2 + np.random.randn(noof) * 0.5 + ticks / 100), 1, 8).astype(int) 
    low_no_gru_2 = np.clip((np.sin(ticks / 55) * 1.5 + np.random.randn(noof) * 0.4 + ticks / 105), 1, 7).astype(int) 
    low_no_gru_3 = np.clip((np.sin(ticks / 60) * 1 + np.random.randn(noof) * 0.3 + ticks / 110), 1, 6).astype(int) 
        
    # Re-plot the graphs based on the new understanding
    # High traffic scenario
    plot_traffic_scenario(ticks, high_gru_1, high_gru_2, high_gru_3, high_no_gru_1, high_no_gru_2, high_no_gru_3, 'High Traffic Scenario', 'HighTraffic')

    # Medium traffic scenario
    plot_traffic_scenario(ticks, medium_gru_1, medium_gru_2, medium_gru_3, medium_no_gru_1, medium_no_gru_2, medium_no_gru_3, 'Medium Traffic Scenario', 'MediumTraffic')

    # Low traffic scenario
    plot_traffic_scenario(ticks, low_gru_1, low_gru_2, low_gru_3, low_no_gru_1, low_no_gru_2, low_no_gru_3, 'Low Traffic Scenario', 'LowTraffic')

