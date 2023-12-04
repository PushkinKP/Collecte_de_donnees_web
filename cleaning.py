######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

# Fais avec Vscode, Python 3.11.1

import pandas as pd
import numpy as np

data = pd.read_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Cnockaert Jules SAE 3-01-VCOD Collecte automatisée de données Web/Data.csv")

for i in data.columns:
    if data[i].dtype == "object":
        data[i] = data[i].str.replace(" \(\?\)", "", regex=False)
        data[i] = data[i].fillna("Unknown")
    if data[i].dtype == "float64":
        data[i] = data[i].replace([np.inf, -np.inf], np.nan) 
        data[i] = data[i].fillna(np.nan) 
        data[i] = data[i].astype("Int64") 
    if data[i].dtype == "int64":
        data[i] = data[i].fillna(np.nan)

data.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Cnockaert Jules SAE 3-01-VCOD Collecte automatisée de données Webt/Data_final.csv", index=False)

