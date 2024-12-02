# Reimport necessary libraries
import numpy as np
import matplotlib.pyplot as plt


def function(noof):
    No_of_ticks = noof
    # Define the ticks again
    ticks = np.arange(0, No_of_ticks, 1)

    # Generate more ic delay data for gru and Normal network scenarios using random walk patterns

    # High Traffic Delay - gru and Normal
    delay_high_gru_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.3, len(ticks)) + np.random.choice([0, 5], len(ticks), p=[0.9, 0.1])))
    delay_high_normal_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.4, len(ticks)) + np.random.choice([0, 8], len(ticks), p=[0.8, 0.2])))

    # Medium Traffic Delay - gru and Normal
    delay_medium_gru_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.2, len(ticks)) + np.random.choice([0, 3], len(ticks), p=[0.9, 0.1])))
    delay_medium_normal_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.3, len(ticks)) + np.random.choice([0, 5], len(ticks), p=[0.85, 0.15])))

    # Low Traffic Delay - gru and Normal
    delay_low_gru_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.1, len(ticks)) + np.random.choice([0, 2], len(ticks), p=[0.95, 0.05])))
    delay_low_normal_ic = np.maximum(0, np.cumsum(np.random.normal(0, 0.2, len(ticks)) + np.random.choice([0, 3], len(ticks), p=[0.9, 0.1])))

    # Plot the more ic delay graphs
    fig, axs = plt.subplots(3, 1, figsize=(14, 14))

    # High traffic plot
    axs[0].plot(ticks, delay_high_gru_ic, label="High Traffic gru", color="blue")
    axs[0].plot(ticks, delay_high_normal_ic, label="High Traffic Normal", color="orange")
    axs[0].set_title("Delay vs Tick - High Traffic ")
    axs[0].set_xlabel("Tick")
    axs[0].set_ylabel("Delay (ticks)")
    axs[0].legend()

    # Medium traffic plot
    axs[1].plot(ticks, delay_medium_gru_ic, label="Medium Traffic gru", color="green")
    axs[1].plot(ticks, delay_medium_normal_ic, label="Medium Traffic Normal", color="red")
    axs[1].set_title("Delay vs Tick - Medium Traffic ")
    axs[1].set_xlabel("Tick")
    axs[1].set_ylabel("Delay (ticks)")
    axs[1].legend()

    # Low traffic plot
    axs[2].plot(ticks, delay_low_gru_ic, label="Low Traffic gru", color="purple")
    axs[2].plot(ticks, delay_low_normal_ic, label="Low Traffic Normal", color="brown")
    axs[2].set_title("Delay vs Tick - Low Traffic ")
    axs[2].set_xlabel("Tick")
    axs[2].set_ylabel("Delay (ticks)")
    axs[2].legend()

    plt.tight_layout()
    plt.savefig(f'plots/delay.png')
    plt.close()

