# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:22:45 2023

@author: LeonardoDiasdaRosa
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = ["testing_region3", "training_region3"]
    conditions = ["normal", "mass_2", "aerodynamic_2", "erosion_2"]

    fft_plot = plt.figure(figsize=[16,12], layout='tight')

    ax1 = fft_plot.gca()

    for data_type in data:
        for condition in conditions:
            
            if condition == "normal":
                line_color = "blue"
                condition_label = "Normal"
                
            elif condition == "erosion_2":
                line_color = "cyan"
                condition_label = "Erosion"
                
            elif condition == "mass_2":
                line_color = "red"
                condition_label = "Mass imbalance"
                
            elif condition == "aerodynamic_2":
                line_color = "yellow"
                condition_label = "Aerodynamic imbalance"
            
            file = condition + '_' + data_type + "fft.csv"
            rotor_speed_fft = pd.read_csv("csv_data/"+file).T

            for column in rotor_speed_fft.columns:
                frequency_data = rotor_speed_fft[column].values
                frequency_data = [float(f) for f in frequency_data]
                        
                N = len(frequency_data)
                n = np.arange(N)
                T = N/20
                freq = n/T 
                
                x_axis = rotor_speed_fft.index
                x_axis = [float(x) for x in x_axis]
                ax1.plot(freq, frequency_data,
                        color=line_color, label=condition_label)

    ax1.set_ylim([0, 0.02])
    ax1.set_xlim([0.2, 0.5])
    ax1.tick_params(labelsize=20)

    handles, labels = ax1.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    lgnd = plt.legend(by_label.values(), by_label.keys(),
                    fontsize=20, frameon=True, loc='upper right')
    lgnd.legendHandles[0]._sizes = [200]
    lgnd.legendHandles[1]._sizes = [200]
    lgnd.legendHandles[2]._sizes = [200]
    lgnd.legendHandles[3]._sizes = [200]

    ax1.set_title("FFT plot of wind turbine RPM (Region 3)", fontsize=30)
    ax1.set_xlabel("Frequency (Hz)", fontsize=20)
    ax1.set_ylabel("RPM", fontsize=20)

    fft_plot.savefig("fft_plot.png", dpi=800)


if __name__ == "__main__":
    main()
