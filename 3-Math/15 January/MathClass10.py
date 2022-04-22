# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:34:13 2021

@author: Ana Beatriz Varela
"""

'''
Histogram
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x
plt.hist(y,100,density=1)
plt.show()
plt.plot(x,y)
plt.show()

'''
Uniform histogram
'''
from scipy.stats import uniform
import matplotlib.pyplot as plt
data=uniform.rvs(size=10000,loc=5,scale=10)
ax=plt.hist(data,bins=30)
plt.show()

'''
Histogram with quadratic func
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.hist(y,100,density=1)
plt.show()

'''
Exponential distrubution
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
x=np.linspace(0.001,10,100)
pdf=expon.pdf(x)
plt.plot(x,pdf,'r-',lw=2,alpha=0.6,label='expon pdf')
plt.show()
y=2**x
plt.hist(y,100,density=1)
plt.show()

'''
Histogram with cubic function
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**3
plt.hist(y,100,density=1)
plt.show()
plt.plot(x,y)
plt.show()

'''
Histogram from a sin function
'''
import numpy as np
import matplotlib.pyplot as plt
n=1000
x=np.linspace(0,6*np.pi,n)
sigl=np.sin(x)
plt.hist(sigl,100)
plt.show()
plt.plot(x,sigl)
plt.show()

'''
Gaussian dist
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(loc=1,scale=2,size=1000) #loc=mean scale=standard deviation size=shape of array
plt.hist(x)
plt.show()

'''
Comparing
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(loc=1,scale=2,size=1000)
y=np.random.normal(loc=1,scale=0.5,size=1000)
plt.hist(x)
plt.hist(y)
plt.show()

'''
Using scipy
'''
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(loc=0,size=1000)
mean,std=norm.fit(data)
plt.hist(data,bins=30,density=True,edgecolor='black')
xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,1000)
y=norm.pdf(x,mean,std)
plt.plot(x,y)
plt.show()

'''
Example of distribution
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd
def random_samples(population,sample_qty,sample_size):
    sample_means=[]
    for i in range(sample_qty):
        sample=rd.sample(population,sample_size)
        sample_mean=np.array(sample).mean()
        sample_means.append(sample_mean)
    return sample_means
uniform=np.random.rand(100000)
print('mean =',np.mean(uniform))
plt.figure(figsize=(7,4))
plt.title('Distribution',fontsize=15)
plt.hist(uniform,100)

samples_from_normal=random_samples(list(uniform),10,10)
plt.figure()
plt.title('Distribution Results',fontsize=15)
sns.distplot(samples_from_normal,color='g')

# *********************************