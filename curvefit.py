# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 13:06:34 2025

@author: Hargi
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


#-----------------------------------VARIABLES--------------------------------


x = np.array([12.5,23.8,40.1,50.9,100])
y = np.array([3.22,3.17,3.15,3.148,3.142])


#-------------------------------------FUNCTIONS-------------------------------

def curvefit(x, A, B, C, D):
    #print(np.array([A,B,C,D]))
    
    return -A * np.log(abs(B*x + C)) + D



popt, pcov = curve_fit(curvefit, x, y, p0=[1, 1, 0, 0])  


yfit = curvefit(x,*popt)

squaresum = np.sum((y-yfit)**2)

totsqsum = np.sum(y-np.mean(y)**2)

Rsquared = 1-squaresum/totsqsum

print("your Rsquared value is",Rsquared)

#--------------------------------------PLOT------------------------------------
plt.figure()


plt.scatter(x, y, label="Values of pi")


plt.axhline(y=np.pi , linestyle = "--")

plt.plot(x, curvefit(x, *popt), color='red', label="Fit")

plt.legend()

