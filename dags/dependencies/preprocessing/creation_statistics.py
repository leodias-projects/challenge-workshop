# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:29:14 2022

@author: LeonardoDiasdaRosa
"""

import pandas as pd
import numpy as np
import os

def main():

    saving_path = 'csv_data/'

    if not os.path.exists(saving_path):
        os.mkdir(saving_path)
    data = ["testing_region3", "training_region3"]

    conditions = ["normal", "erosion_2", "mass_2", "aerodynamic_2"]

    for data_type in data:
        for condition in conditions:
            new_df = pd.DataFrame(columns=['WS_Avg', 'WS_Std',
                                           'RPM_Avg','NcIMUTaXsSTD',
                                           'NcIMUTaYsSTD', 'Pitch_Avg'])
            pos = 0
            saving_name = condition + '_' + data_type
            if not os.path.exists(saving_path+saving_name+".csv"):
                print("Saving " + saving_name)
                wind_speeds = os.listdir(data_type+'/'+condition)
                for speed in wind_speeds:
                    files = os.listdir(data_type+'/'+condition+'/'+speed)
                    path = data_type + '/' + condition + '/' + speed + '/'
                    for file in files:
                        file_data = open(path+file).read().splitlines()
                        temp_file = "temp_file_stats.out"
                        with open(temp_file, 'w') as fast_data:
                    
                            for line, content in enumerate(file_data):
                                if line > 5 and line != 7:  
                                    fast_data.write(content+'\n')
                    
                        data = pd.read_csv(temp_file, delimiter = "\t") 
                        
                        wind_speed = data.loc[600:,'Wind1VelX']
                        wind_speed = [float(x) for x in wind_speed]
                        wind_speed_std = np.std(wind_speed)
                        wind_speed = np.mean(wind_speed)
                        wind_speed_std = (wind_speed_std / wind_speed) *100
                        
                        rotor_speed = data.loc[600:,'RotSpeed']
                        rotor_speed = [float(x) for x in rotor_speed]
                        rotor_speed = np.mean(rotor_speed)
                        
                        fa_acc = data.loc[600:,'NcIMUTAxs']
                        fa_acc = [float(x) for x in fa_acc]
                        fa_acc_std = np.std(fa_acc)
                        fa_acc = np.mean(fa_acc)
                        
                        ss_acc = data.loc[600:,'NcIMUTAys']
                        ss_acc = [float(x) for x in ss_acc]
                        ss_acc_std = np.std(ss_acc)
                        ss_acc = np.mean(ss_acc)
                        
                        power = data.loc[600:,'GenPwr']
                        power = [float(x) for x in power]
                        power = np.mean(power)
                        
                        bld_pitch_1 = data.loc[600:, 'BldPitch1'].values
                        bld_pitch_1=[float(x) for x in bld_pitch_1]      
                        bld_pitch_1 = np.mean(bld_pitch_1)
                        bld_pitch_2 = data.loc[600:, 'BldPitch2'].values
                        bld_pitch_2=[float(x) for x in bld_pitch_2]
                        bld_pitch_2 = np.mean(bld_pitch_2)            
                        bld_pitch_3 = data.loc[600:, 'BldPitch3'].values
                        bld_pitch_3=[float(x) for x in bld_pitch_3]
                        bld_pitch_3 = np.mean(bld_pitch_3)
                        
                        pitch_avg = np.mean([bld_pitch_1, bld_pitch_2, bld_pitch_3])
                
                        row=[wind_speed, wind_speed_std,
                            rotor_speed, fa_acc_std, 
                            ss_acc_std, pitch_avg]
                        
                        new_df.loc[pos] = row
                        pos = pos + 1
                        os.remove(temp_file)
                new_df.to_csv(saving_path+saving_name+".csv",index=False)
            else:
                print(saving_name + "Already exists! Skipping overwrite")


if __name__ == "__main__":
    main()
