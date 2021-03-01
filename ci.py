# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:31:11 2019

@author: CADD
"""
#Correlation

import pandas as pd
df = pd.read_csv("r'E:\Rani DS\New folder\mtcars.csv'")  
df.corr(method ='pearson') 


import pandas as pd
import scipy.stats as stats
z=stats.norm.ppf(0.95,0,1)
import numpy as np
data=pd.read_csv(r'E:\Rani DS\New folder\mtcars.csv')
data
X = data.iloc[:,1:].values  
print(X)
n=len(X)
m=X.mean()
mg=z*(np.std(data)/np.sqrt(n))
upperCI=m+mg
print(upperCI)
lowerCI=m-mg
print(lowerCI)

#t-distribution
# define probability
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
# seed the random number generator
seed(10)
# generate two independent samples
data1 = 5 * randn(100) + 50
data1
data2 = 5 * randn(100) + 51
data2
# compare samples
stat,p = ttest_ind(data1, data2)
#print('t=%.4f, p=%.3f' % (stat, p))
if(p<0.05):
    print('Reject null hypothesis that the means are equal.')
else:
	print('accept the alternate hypothesis that the means are different.')
    
    
