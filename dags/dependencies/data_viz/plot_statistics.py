# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:38:23 2022

@author: LeonardoDiasdaRosa
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    normal_training = pd.read_csv('csv_data/normal_training_region3.csv')
    mass_training = pd.read_csv('csv_data/mass_2_training_region3.csv')
    aerodynamic_training = pd.read_csv('csv_data/aerodynamic_2_training_region3.csv')
    erosion_training = pd.read_csv('csv_data/erosion_2_training_region3.csv')
    
    rotor_speed_avg = 'RPM_Avg'
    blade_pitch_avg = 'Pitch_Avg'
    nc_imu_ta_xs_std = 'NcIMUTaXsSTD'
    nc_imu_ta_ys_std = 'NcIMUTaYsSTD'
    
    dot_size = 100

    tickssize = 15
    xticks = 15
    legendfont = 20
    titlefont = 30
    subplotitlefont = 26
    
    normal_color = '#58DAE7'
    mass_imbalance_color = '#8ECA35'
    aerodynamic_imbalance_color = '#CA3543'
    erosion_color = '#7135CA'
    
    main_title = ''
    plot1_title = 'Rotor speed avereage'
    plot2_title = 'Blade pitch angle average'
    plot3_title = 'Standard deviation - NcIMUTaXs'
    plot4_title = 'Standard deviation - NcIMUTaYs'
    # %% ====================================== A ===============================
    fig = plt.figure(figsize=(18, 12), layout='tight')
    fig.suptitle(main_title,
                 fontsize=titlefont)
    
    # Normal
    ax1 = plt.subplot(2, 2, 1)
    plt.title(plot1_title, fontsize=subplotitlefont)
    wind_speed = normal_training.loc[:, 'WS_Avg']
    var = normal_training.loc[:, rotor_speed_avg]
    
    ax1.scatter(wind_speed, var, label='Normal',
                marker='o', s=dot_size, color=normal_color)
    
    # Mass Imbalance
    wind_speed = mass_training.loc[:, 'WS_Avg']
    var = mass_training.loc[:, rotor_speed_avg]
    
    ax1.scatter(wind_speed, var, label='Mass Imb.',
                marker='o', s=dot_size, color=mass_imbalance_color)
    
    # Pitch Error
    wind_speed = aerodynamic_training.loc[:, 'WS_Avg']
    var = aerodynamic_training.loc[:, rotor_speed_avg]
    
    ax1.scatter(wind_speed, var, label='Aerodynamic Imb.',
                marker='o', s=dot_size, color=aerodynamic_imbalance_color)
    
    # Erosion
    wind_speed = erosion_training.loc[:, 'WS_Avg']
    var = erosion_training.loc[:, rotor_speed_avg]
    
    ax1.scatter(wind_speed, var, label='Erosion', marker='o',
                s=dot_size, color=erosion_color)
    
    handles, labels = ax1.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    lgnd = plt.legend(by_label.values(), by_label.keys(),
                      fontsize=legendfont, frameon=True, loc='upper left')
    lgnd.legendHandles[0]._sizes = [80]
    lgnd.legendHandles[1]._sizes = [80]
    lgnd.legendHandles[2]._sizes = [80]
    lgnd.legendHandles[3]._sizes = [80]
    plt.xticks(size=xticks)
    plt.yticks(size=tickssize)
    plt.ylabel("RPM", fontsize=20)
    #plt.ylabel("$^\circ$", fontsize=40)
    plt.ylim([19.5, 20.5])
    plt.xlim([13.5, 18])
    # %% ====================================== B ===============================
    ax2 = plt.subplot(2, 2, 2)
    plt.title(plot2_title, fontsize=subplotitlefont)
    
    wind_speed = normal_training.loc[:, 'WS_Avg']
    var = normal_training.loc[:, blade_pitch_avg]
    
    ax2.scatter(wind_speed, var, label='Normal',
                marker='o', s=dot_size, color=normal_color)
    
    # Mass Imbalance
    wind_speed = mass_training.loc[:, 'WS_Avg']
    var = mass_training.loc[:, blade_pitch_avg]
    
    ax2.scatter(wind_speed, var, label='Mass Imb.',
                marker='o', s=dot_size, color=mass_imbalance_color)
    
    # Pitch Error
    wind_speed = aerodynamic_training.loc[:, 'WS_Avg']
    var = aerodynamic_training.loc[:, blade_pitch_avg]
    
    ax2.scatter(wind_speed, var, label='Aerodynamic Imb.',
                marker='o', s=dot_size, color=aerodynamic_imbalance_color)
    
    # Erosion
    wind_speed = erosion_training.loc[:, 'WS_Avg']
    var = erosion_training.loc[:, blade_pitch_avg]
    
    ax2.scatter(wind_speed, var, label='Erosion',
                marker='o', s=dot_size, color=erosion_color)
    
    plt.ylabel("Degrees", fontsize=20)
    plt.xticks(size=xticks)
    plt.yticks(size=tickssize)
    plt.ylim([11, 16])
    plt.xlim([14, 17])
    # %% ====================================== C ===============================
    ax3 = plt.subplot(2, 2, 3)
    plt.title(plot3_title, fontsize=subplotitlefont)
    wind_speed = normal_training.loc[:, 'WS_Avg']
    var = normal_training.loc[:, nc_imu_ta_xs_std]
    
    ax3.scatter(wind_speed, var, label='Normal',
                marker='o', s=dot_size, color=normal_color)
    
    # Mass Imbalance
    wind_speed = mass_training.loc[:, 'WS_Avg']
    var = mass_training.loc[:, nc_imu_ta_xs_std]
    
    ax3.scatter(wind_speed, var, label='Mass Imb.',
                marker='o', s=dot_size, color=mass_imbalance_color)
    
    # Pitch Error
    wind_speed = aerodynamic_training.loc[:, 'WS_Avg']
    var = aerodynamic_training.loc[:, nc_imu_ta_xs_std]
    
    ax3.scatter(wind_speed, var, label='Aerodynamic Imb.',
                marker='o', s=dot_size, color=aerodynamic_imbalance_color)
    
    # Erosion
    wind_speed = erosion_training.loc[:, 'WS_Avg']
    var = erosion_training.loc[:, nc_imu_ta_xs_std]
    
    ax3.scatter(wind_speed, var, label='Erosion',
                marker='o', s=dot_size, color=erosion_color)
    
    plt.ylabel("m/$s^2$", fontsize=20)
    
    plt.xticks(size=xticks)
    plt.yticks(size=tickssize)
    plt.xlim([13.5, 18])
    # %% ====================================== D ===============================
    ax4 = plt.subplot(2, 2, 4)
    plt.title(plot4_title, fontsize=subplotitlefont)
    wind_speed = normal_training.loc[:, 'WS_Avg']
    var = normal_training.loc[:, nc_imu_ta_ys_std]
    
    ax4.scatter(wind_speed, var, label='Normal',
                marker='o', s=dot_size, color=normal_color)
    
    # Erosion
    wind_speed = erosion_training.loc[:, 'WS_Avg']
    var = erosion_training.loc[:, nc_imu_ta_ys_std]
    
    plt.scatter(wind_speed, var, label='Erosion',
                marker='o', s=dot_size, color=erosion_color)

    # Mass Imbalance
    wind_speed = mass_training.loc[:, 'WS_Avg']
    var = mass_training.loc[:, nc_imu_ta_ys_std]
    
    ax4.scatter(wind_speed, var, label='Mass Imb.',
                marker='o', s=dot_size, color=mass_imbalance_color)
    
    # Pitch Error
    wind_speed = aerodynamic_training.loc[:, 'WS_Avg']
    var = aerodynamic_training.loc[:, nc_imu_ta_ys_std]
    
    ax4.scatter(wind_speed, var, label='Aerodynamic Imb.',
                marker='o', s=dot_size, color=aerodynamic_imbalance_color)
    
    plt.xticks(size=xticks)
    plt.yticks(size=tickssize)
    plt.xlim([13.5, 18])
    
    plt.savefig("statistics_plot.png", dpi=800)
    
    
if __name__ == "__main__":
    main()
