# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:33:11 2019

@author: LIVE WIRE
"""
"1 sample-tests whether the mean of a population is significantly different than a sample mean
"paired-tests whether the difference in means of two depenendent samples is significantly different
"independent-tests whether the difference in means of two independent samples is significantly different"

'If abs(t-statistic) <= critical value: Reject null hypothesis that the means are equal.'
'If abs(t-statistic) > critical value: accept the null hypothesis that the means are equal.'
   ' If p > alpha: Accept null hypothesis that the means are equal.'
       'If p <= alpha: Reject null hypothesis that the means are equal.'
       
       
'T Test    -independent t test'
#Tests whether the means of two independent samples are significantly different.  
from scipy.stats import ttest_ind
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = ttest_ind(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print(' Probably different distributions')
    
    
#Tests whether the means of two paired samples are significantly different.

# Example of the Paired t-test
from scipy.stats import ttest_rel
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = ttest_rel(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
    
    #one sample test
from scipy import stats as ss
import numpy as np
#seed(100)
data1 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
print(data1)
true_mu=0
stat,p= ss.ttest_1samp(data1, true_mu)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print("Probably the same distribution")
else:
    print("Probably different distributions")


#Anova test
    #Tests whether the means of two or more independent samples are significantly different
from scipy.stats import f_oneway
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]
stat, p = f_oneway(data1, data2, data3)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')



#chi square test
''' two categorical variables from a single population. determine whether there is a significant association bw the two variables.
In election survey, voters - gender (male or female), voting preference (Democrat, Republican, or Independent).
 determine whether gender is related to voting preference'''
from scipy.stats import chi2_contingency
table = [[10, 20, 30],[6,  9,  17]]
stat, p, dof, expected = chi2_contingency(table)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')
    
    
    
    

# Example of the Mann-Whitney U Test
from scipy.stats import mannwhitneyu
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = mannwhitneyu(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')