# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:11:02 2021

@author: Ana Beatriz Varela
"""

'''
Statistics
'''
'''
Geometric mean
'''
data = [7.0,8.0,8.5]
geo_mean = (7*8*8.5)**(1/(len(data)))
print(geo_mean)             # 7.807925321779708

'''
Variace
'''
import numpy as np

var2 = (((7-7.83)**2)+((8-7.83)**2)+((8.5-7.83)**2))/(3-1)
var = np.sqrt(var2)
print(var)                  # 0.7637735266425513

'''
example 2
'''
import numpy as np

data = [10,30,50]
mean = ((10+30+50)/3)
var2 = (((data[0]-mean)**2)+((data[1]-mean)**2)+((data[2]-mean)**2))/(len(data)-1)
var = np.sqrt(var2)
print(var)                  # 20.0

'''
Standart deviation
'''
import numpy as np
# sd = sqrt(variance)

var = 20
sd = np.sqrt(20)
print(sd)                   # 4.47213595499958

'''
Quartile
'''
import pandas as pd

data = [3, 6, 7, 11, 13, 22, 30, 40, 44, 50, 52, 61, 68, 80, 94]
q1 = 11
q2 = 40
q3 = 61
q4 = 90

df = pd.DataFrame(data)
print(df.describe())
#                0
# count  15.000000
# mean   38.733333
# std    28.766217
# min     3.000000
# 25%    12.000000
# 50%    40.000000
# 75%    56.500000
# max    94.000000

print(df.quantile(0.5)) # 50% quartile
# 0    40.0
# Name: 0.5, dtype: float64

quartiles = pd.qcut(data,3)
print(quartiles)
# [(2.999, 19.0], (2.999, 19.0], (2.999, 19.0], (2.999, 19.0], (2.999, 19.0], ..., (50.667, 94.0], (50.667, 94.0], (50.667, 94.0], (50.667, 94.0], (50.667, 94.0]]
# Length: 15
# Categories (3, interval[float64]): [(2.999, 19.0] < (19.0, 50.667] < (50.667, 94.0]]
                                                                      
'''
Sampling

Random sample
'''
import random

Sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("With list:", random.sample(Sample, 5))       # With list: [10, 5, 4, 7, 9]

'''
Systematic sample
'''
import numpy as np

systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 2
print(np.mean(sample))          # 8.0
size = int(len(sample)/step)

for i in range(0,size):
    systematic_sample.append(sample[i*step])
print(systematic_sample)        # [1, 3, 5, 7, 9]

systematic_mean = np.mean(systematic_sample)
print(systematic_mean)          # 5.0

'''
Another way to do this:
'''
import numpy as np

systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 2

for i in range(0,15,step):
    systematic_sample.append(sample[i])
print(systematic_sample)        # [1, 3, 5, 7, 9, 11, 13, 15]

systematic_mean=np.mean(systematic_sample)
print(systematic_mean)          # 8.0

'''
Cluster sample
'''
import numpy as np

systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 3
print(np.mean(sample))          # 8.0
size = int(len(sample)/step)

for i in range(0,size):
    systematic_sample.append(sample[i*step])
    systematic_sample.append(sample[i*step]+1)
systematic_mean = np.mean(systematic_sample)
print(systematic_mean)          # 7.5

'''
Stratified sample
'''
import random 
import numpy as np

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]
systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
A, B, C = split_list(sample, 3)
total= split_list(sample, 3)
stratified_list =[]
print('mean all values:', np.mean(sample) )         # mean all values: 8.0
splited_list = [A, B, C]

for i in range(0,len(splited_list)):
    stratified_list.append(splited_list[i][random.randint(0,4)])
systematic_mean = np.mean(stratified_list)
print('stratified mean', systematic_mean)           # stratified mean (random value)

'''
Scipy
'''
import numpy as np
from scipy import stats
from scipy.stats import gmean
from scipy.stats import hmean
import random

numbers = [ 1, 1, 2, 2, 3, 3, 4, 1, 2 ]
print(numbers)          
# [1, 1, 2, 2, 3, 3, 4, 1, 2]

Mean = np.mean(numbers)
Median = np.median(numbers)
Mode = int(stats.mode(numbers)[0]) # index 1 gives frequency
print("Mean = ", Mean, "\nMedian = ", Median, "\nMode = ", Mode)
# Mean =  2.111111111111111 
# Median =  2.0 
# Mode =  1

Geometric_Mean = gmean(numbers)
Harmonic_mean = hmean(numbers)
print("Geometric Mean = ", Geometric_Mean, "\nHarmonic Mean = ", Harmonic_mean)
# Geometric Mean =  1.8761425449123872 
# Harmonic Mean =  1.6615384615384616

Variance = np.var(numbers)
Standard_Deviation = np.std(numbers)
print("Variance = ", Variance, "\nStandard deviation = ", Standard_Deviation)
# Variance =  0.9876543209876544 
# Standard deviation =  0.9938079899999066

Q1 = np.percentile(numbers, 25)
Q2 = np.percentile(numbers, 50)
Q3 = np.percentile(numbers, 75)
print("Q1 = ", Q1, "\nQ2 = ", Q2, "\nQ3 = ", Q3) # 1 1 1 2 2 2 3 3 
# Q1 =  1.0 
# Q2 =  2.0 
# Q3 =  3.0

'''
Statistics exercises

1.
'''
import numpy as np

data = [4,7,2,9,12,2,20,10,5,9]
data.sort()
if len(data)%2!=0:
    median = data[(int(len(data)/2))]
else:
    median = (((data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))-1)]))/2)
print("The median is {}".format(median))        # The median is 8.0

'''
Another way to do this:
'''
median = np.median(data)
print("The median is {}".format(median))        # The median is 8.0

quartile_div=len(data)/3
if (np.round(quartile_div)*3)!=len(data):
    q1=data[:int(np.round(quartile_div))]
    q2=data[int(np.round(quartile_div)):int((np.round(quartile_div)*2)+1)]
    q3=data[int((np.round(quartile_div)*2)+1):]
    
else:
    q1=data[:int(np.round(quartile_div))]
    q2=data[int(np.round(quartile_div)):int((np.round(quartile_div)*2))]
    q3=data[int((np.round(quartile_div)*2)):]
    
x025=(q1[0]+q1[2])/2
x075=(q3[0]+q3[1])/2
x05=x075-x025
print("The quartiles are",q1,q2,q3,"with a lower range of",x025,"an upper range of",x075,"and an inner-quartile range of",x05)
# The quartiles are [2, 2, 4] [5, 7, 9, 9] [10, 12, 20] with a lower range of 3.0 an upper range of 11.0 and an inner-quartile range of 8.0

'''
2.
'''
import numpy as np

xi = [2,5,10,11]
s = 0
for n in xi:
    s+=n
mean=s/len(xi)

'''
Another way to do this:
'''
mean=np.mean(xi)
print("The mean is",mean)                   # The mean is 7.0
var_up_sum=0
for n in xi:
    var_up_sum+=((n-mean)**2)
variance=var_up_sum/(len(xi)-1)
print("With a variance of",variance)        # With a variance of 18.0
std=np.sqrt(variance)
print("And a standard deviation of",std)    # And a standard deviation of 4.242640687119285

'''
3.
'''
import numpy as np

data=[4,1,2,1,3,2,1,1]
data.sort()
try:
    median=data[(int(len(data)/2))]
except:
    median=(data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))+1)])/2
print("The median is {}".format(median))    # The median is 2

'''
4.
'''
import numpy as np

mean=np.mean(data)
var_up_sum=0

for n in data:
    var_up_sum+=((n-mean)**2)
variance=var_up_sum/(len(data)-1)
std=np.sqrt(variance)

print("The standard deviation is",std)      # The standard deviation is 1.1259916264596033

'''
Calculate Portugal's mode, median, variance and standard deviation for
boys and girls over the years for 4 countries
'''
import numpy as np

B_AUS=[527.0,527.0,519.0,510.1,497.0,494.0]
G_AUS=[522.0,513.0,509.0,497.82,491.0,488.0]
B_CAN=[541.0,534.0,533.0,523.2,520.0,514.0]
G_CAN=[530.0,520.0,521.0,513.02,511.0,510.0]
B_CZK=[524.0,514.0,495.0,504.7,496.0,501.0]
G_CZK=[509.0,504.0,490.0,492.9,489.0,498.0]
B_POR=[472.0,474.0,493.0,492.7,497.0,497.0]
G_POR=[460.0,459.0,481.0,481.3,487.0,488.0]

def meadian(data):
    try:
        median=data[(int(len(data)/2))]
    except:
        median=(data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))+1)])/2
    return median

def mode(data):
    all_mode=dict()
    for i in data:
        if str(i) not in all_mode.keys():
            all_mode[str(i)]=1
        else:
            all_mode[str(i)]+=1
    M_times=1
    mode=[]
    for i in all_mode.items():
        if i[1]>=M_times:
            if M_times==i[1]:
                mode.append(float(i[0]))
            else:
                M_times=i[1]
                mode=[float(i[0])]
        else:
            pass
    if M_times==1:
        mode="no mode"
    else:
        pass
    return mode

def variance(data):
    mean=np.mean(data)
    var_up_sum=0
    for i in data:
        var_up_sum+=((i-mean)**2)
    variance=var_up_sum/(len(data)-1)
    return variance

import numpy as np
B_AUS_data={'gender':'boys','country':'Australia','mode':mode(B_AUS),'median':meadian(B_AUS),'variance':variance(B_AUS),'standard deviation':np.sqrt(variance(B_AUS))}
G_AUS_data={'gender':'girls','country':'Australia','mode':mode(G_AUS),'median':meadian(G_AUS),'variance':variance(G_AUS),'standard deviation':np.sqrt(variance(G_AUS))}
B_CAN_data={'gender':'boys','country':'Canada','mode':mode(B_CAN),'median':meadian(B_CAN),'variance':variance(B_CAN),'standard deviation':np.sqrt(variance(B_CAN))}
G_CAN_data={'gender':'girls','country':'Canada','mode':mode(G_CAN),'median':meadian(G_CAN),'variance':variance(G_CAN),'standard deviation':np.sqrt(variance(G_CAN))}
B_CZK_data={'gender':'boys','country':'Czech Republic','mode':mode(B_CZK),'median':meadian(B_CZK),'variance':variance(B_CZK),'standard deviation':np.sqrt(variance(B_CZK))}
G_CZK_data={'gender':'girls','country':'Czech Republic','mode':mode(G_CZK),'median':meadian(G_CZK),'variance':variance(G_CZK),'standard deviation':np.sqrt(variance(G_CZK))}
B_POR_data={'gender':'boys','country':'Portugal','mode':mode(B_POR),'median':meadian(B_POR),'variance':variance(B_POR),'standard deviation':np.sqrt(variance(B_POR))}
G_POR_data={'gender':'girls','country':'Portugal','mode':mode(G_POR),'median':meadian(G_POR),'variance':variance(G_POR),'standard deviation':np.sqrt(variance(G_POR))}
all_data=[B_AUS_data,G_AUS_data,B_CAN_data,G_CAN_data,B_CZK_data,G_CZK_data,B_POR_data,G_POR_data]

for data in all_data:
    if type(data['mode'])=='string':
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'],',',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))
        # In Portugal the girls math scores have no mode , 481.3 of median, 172.62 of variance, and 13.14 of standard deviation
    elif len(data['mode'])==1:
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'][0],'of mode,',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))
        # In Portugal the girls math scores have n of mode, 481.3 of median, 172.62 of variance, and 13.14 of standard deviation
    else:
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'],',',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))
        # In Portugal the girls math scores have no mode , 481.3 of median, 172.62 of variance, and 13.14 of standard deviation

# *********************************