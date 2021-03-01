# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:05:04 2019

@author: LIVE WIRE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import os; os.getcwd()
#%%

df = pd.read_csv(r'E:\Rani DS\New folder\creditcard.csv')
print(df.shape)
df.head()   
df.info()
df.describe()
class_names = {0:'Not Fraud', 1:'Fraud'}
print(df.Class.value_counts().rename(index = class_names))
from sklearn.model_selection import train_test_split
feature_names = df.iloc[:, 1:30].columns
feature_names
target = df.iloc[:1, 30: ].columns
target
print(feature_names)
#%%print(target)
data_features = df[feature_names]
data_target = df[target]
X_train, X_test, y_train, y_test = train_test_split(data_features, data_target, train_size=0.70, test_size=0.30)
print("Length of X_train is: {X_train}".format(X_train = len(X_train)))
print("Length of X_test is: {X_test}".format(X_test = len(X_test)))
print("Length of y_train is: {y_train}".format(y_train = len(y_train)))
print("Length of y_test is: {y_test}".format(y_test = len(y_test)))
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score
model = LogisticRegression()
model.fit(X_train, y_train.values.ravel())
pred = model.predict(X_test)
pred
class_names = ['not_fraud', 'fraud']
matrix = confusion_matrix(y_test, pred)
print(matrix)

acc = accuracy_score(y_test, pred)
print(acc)







# Create pandas dataframe
dataframe = pd.DataFrame(matrix, index=class_names, columns=class_names)
# Create heatmap
sns.heatmap(dataframe, annot=True, cbar=None, cmap="Blues", fmt = 'g')
plt.title("Confusion Matrix")
plt.tight_layout()
plt.ylabel("True Class")
plt.xlabel("Predicted Class")
plt.show()
from sklearn.metrics import f1_score, recall_score
f1_score = round(f1_score(y_test, pred), 2)
recall_score = round(recall_score(y_test, pred), 2)
print("Sensitivity/Recall for Logistic Regression Model 1 : {recall_score}".format(recall_score = recall_score))
print("F1 Score for Logistic Regression Model 1 : {f1_score}".format(f1_score = f1_score))
