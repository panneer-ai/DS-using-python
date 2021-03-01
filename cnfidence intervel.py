# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:30:49 2020

@author: SANGAR LOCAL
"""

#confidence intervel:
import scipy.stats as stats

z=stats.norm.ppf(0.975,0,1)
stats.norm.ppf(0.995,0,1)
stats.norm.ppf(0.950,0,1)
t=stats.t.ppf(0.995,139)
stats.t.ppf(0.995,139)
stats.t.ppf(0.950,139)
t
from scipy.stats import sem,t
from scipy import mean
import numpy as np
confidence=0.95
data=[1,2,3,4,5]
n=len(data)
m=mean(data)
m
#z distribution:
mg=z*(np.std(data)/np.sqrt(n))
upperCI =m +mg
print(upperCI)
lowerCI = m-mg
print(lowerCI)
#t distribution:
mg=t(np.std(data)/np.sqrt(n))
upperCI1 = m+mg
lowerCI2 = m-mg