# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:32:41 2022

@author: LeonardoDiasdaRosa
"""

from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
from sklearn.svm import SVC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

def main():
    scaler = StandardScaler()
    plt.close("all")
    # %% Set labels
    normal = 0
    mass_imbalance = 1
    aero_imbalance = 2
    erosion = 3
    column_to_drop = ["RPM_Avg"]
    confusionmatrix_title = ""

    path = "csv_data/"
    # %% Training dataset
    normal_training = pd.read_csv(path+'normal_training_region3.csv')
    mass_training = pd.read_csv(path+'mass_2_training_region3.csv')
    aerodynamic_training = pd.read_csv(path+'aerodynamic_2_training_region3.csv')
    erosion_training = pd.read_csv(path+'erosion_2_training_region3.csv')

    data = pd.concat([normal_training,
                    mass_training, aerodynamic_training,
                    erosion_training])
    data = data.drop(columns=column_to_drop)

    size_normal = len(normal_training)
    size_mass = len(mass_training)
    size_aerodynamic = len(aerodynamic_training)
    size_erosion = len(erosion_training)
    size = size_normal + size_mass + size_aerodynamic + size_erosion

    class_data = np.zeros(size)
    class_data[0:size_normal] = normal

    class_data[size_normal:size_normal + size_mass] = mass_imbalance

    class_data[size_normal + size_mass:
            size_normal + size_mass + size_aerodynamic] = aero_imbalance

    class_data[size_normal + size_mass + size_aerodynamic:
            size_normal + size_mass + size_aerodynamic +
            size_erosion] = erosion

    data['class'] = class_data

    data = shuffle(data)
    features_data_training_notScaled = data.iloc[:, :-1].values
    features_data_training = scaler.fit_transform(features_data_training_notScaled)
    class_data_training = data.iloc[:, -1].values
    # %% Test dataset
    normal_testing = pd.read_csv(path+'normal_testing_region3.csv')
    mass_testing = pd.read_csv(path+'mass_2_testing_region3.csv')
    aerodynamic_testing = pd.read_csv(path+'aerodynamic_2_testing_region3.csv')
    erosion_testing = pd.read_csv(path+'erosion_2_testing_region3.csv')

    data = pd.concat([normal_testing,
                    mass_testing, aerodynamic_testing,
                    erosion_testing])
    data = data.drop(columns=column_to_drop)

    size_normal = len(normal_testing)
    size_mass = len(mass_testing)
    size_aerodynamic = len(aerodynamic_testing)
    size_erosion = len(erosion_testing)
    size = size_normal + size_mass + size_aerodynamic + size_erosion

    class_data = np.zeros(size)
    class_data[0:size_normal] = normal

    class_data[size_normal:size_normal + size_mass] = mass_imbalance

    class_data[size_normal + size_mass:
            size_normal + size_mass + size_aerodynamic] = aero_imbalance

    class_data[size_normal + size_mass + size_aerodynamic:
            size_normal + size_mass + size_aerodynamic +
            size_erosion] = erosion

    data['class'] = class_data
    data = shuffle(data)

    features_data_testing_notScaled = data.iloc[:, :-1].values
    features_data_testing = scaler.fit_transform(features_data_testing_notScaled)
    class_data_testing = data.iloc[:, -1].values
    # %% SVM
    clf = SVC(kernel='rbf', C=70, gamma=0.1, decision_function_shape='ovo')
    clf.fit(features_data_training, class_data_training)
    predictions = clf.predict(features_data_testing)

    accuracy = accuracy_score(class_data_testing, predictions)
    print("The statistic data resulted in an accuracy of " + str(accuracy * 100) + "\% for the model" )
    # %%
    plt.figure(figsize=(12,8), tight_layout=True)
    cf_matrix = confusion_matrix(class_data_testing, predictions)

    ax = sns.heatmap(cf_matrix/np.sum(cf_matrix[0]), annot=True, fmt='.1%',
                    cmap='Blues', cbar=False, annot_kws={'size': 25,
                                                        'fontweight': 'bold'})

    ax.set_title("SVM classification - statistics data", fontsize=30)
    ax.set_xlabel('Labeled', fontsize=25)
    ax.set_ylabel('Real \n', fontsize=25)

    ax.tick_params(axis='both', which='major', labelsize=20)

    ax.xaxis.set_ticklabels(['Normal', 'Mass\nImb.',
                            "Aerodynamic\nImb", "Erosion"])
    ax.yaxis.set_ticklabels(['Normal', 'Mass\nImb.',
                            "Aerodynamic\nImb", "Erosion"])

    ax.set_yticklabels(labels=ax.get_yticklabels(), va='center')
    plt.savefig("SVM_statistics.png", dpi=800)

if __name__ == "__main__":
    main()
