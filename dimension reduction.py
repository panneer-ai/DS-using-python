# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:05:13 2019

@author: User
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# feature values
x = np.random.randn(1000)
y = 2*x
z = np.random.randn(1000)

# target values
t=len(x)*[0] # list of len(x)
for i, val in enumerate(z): #no of counter of iterations
    if x[i]+y[i]+z[i] < 0:
        t[i] = 'N' # negative
    else:
        t[i] = 'P'

# create the dataframe
df = np.column_stack((x, y, z, t))  #take seq of 1d array,make columns inti 2d array
df = pd.DataFrame(df)
print(df.head(10))
 # dataframe for PCA : PCA can not have 'categorical' features
df_temp = df.drop(3, axis=1) # drop the columns
pca = PCA(n_components=2) # 2 dimensional PCA
pca.fit(df_temp)
df_pca = pca.transform(df_temp)
print(df_pca)



import pandas as pd
df= pd.read_csv(r"E:\Rani DS\New folder\iris.csv")
# load dataset into Pandas DataFrame
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
df.head()

from sklearn.preprocessing import StandardScaler
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']

x = df.loc[:, names].values
y = df.loc[:,['Class']].values
x = StandardScaler().fit_transform(x)
x = pd.DataFrame(x)
print(x)

from sklearn.decomposition import PCA#principal component analysis
pca = PCA(n_components=3)#reduce
x_pca = pca.fit_transform(x)
print(x_pca)
x_pca = pd.DataFrame(x_pca)
x_pca.head()

exp_var = pca.explained_variance_ratio_
exp_var


