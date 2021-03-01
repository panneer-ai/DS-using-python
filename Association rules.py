# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:25:05 2019

@author: LIVE WIRE
"""

# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv(r'G:\DATA SCIENCE\Paneer\datas\Market_Basket_Optimisation.csv',header = None)
dataset
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset 
#download (apyori)    
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 2)

# Visualising the results
results = list(rules)
print(results)
