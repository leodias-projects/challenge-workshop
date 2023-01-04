# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:35:53 2022

@author: LeonardoDiasdaRosa
"""

import pandas as pd
import numpy as np
import os
from scipy.fftpack import fft

def main():

    saving_path = 'csv_data/'

    if not os.path.exists(saving_path):
        os.mkdir(saving_path)

    data = ["testing_region3", "training_region3"]

    pos = 1
    conditions = ["normal", "mass_2", "aerodynamic_2", "erosion_2"]

    for data_type in data:
        for condition in conditions:
            saving_name = condition + '_' + data_type
            if not os.path.exists(saving_path+saving_name+"fft.csv"):
                print("Saving " + saving_name +"fft")
                wind_speeds = os.listdir(data_type+'/'+condition)
                frequency_data = []
                for speed in wind_speeds:
                    files = os.listdir(data_type+'/'+condition+'/'+speed)
                    path = data_type + '/' + condition + '/' + speed + '/'
                    for file in files:
                        file_data = open(path+file).read().splitlines()
                        temp_file = "temp_file_fft.out"
                        with open(temp_file, 'w') as fast_data:
                    
                            for line, content in enumerate(file_data):
                                if line > 5 and line != 7:  
                                    fast_data.write(content+'\n')
                    
                        data = pd.read_csv(temp_file, delimiter = "\t") 
                        rotor_speed = data.loc[:, 'RotSpeed'].values 
                        
                        rotor_speed_fft = fft(rotor_speed)
                        rotor_speed_fft = abs(rotor_speed_fft)
                        rotor_speed_fft = (1 / (len(rotor_speed)) * rotor_speed_fft)
                        
                        frequency_data.append(rotor_speed_fft)
                        os.remove(temp_file)
                        
                df = pd.DataFrame(frequency_data)
                df.to_csv(saving_path+saving_name+"fft.csv",index=False)
            else:
                print(saving_name + "Already exists! Skipping overwrite")


if __name__ == "__main__":
    main()