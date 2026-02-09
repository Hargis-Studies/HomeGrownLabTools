# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 23:32:00 2026

@author: Hargi
"""

import numpy as np
import matplotlib.pyplot as plt


#======================GLOBALS============================================



g1 = 9.8
R1= 5
phi1 = 20*(np.pi/180)
t = 0.0
tmax = 10
dt = .01
omega = 0

#=====================FUNCTIONS===========================================

phi1list = [20*(np.pi/180)]
tlist = [0.0]




omegalist = [omega]

def f(phi,omega):
        
    return np.array([omega, g1/R1 *np.sin(phi)])
Approxlist = [20*(np.pi/180)]

while t< tmax:
    k1 = dt*f(phi1,omega) 
    k2 = dt*f(phi1+k1[0]/2, omega + k1[1]/2)
    k3 = dt*f(phi1+k2[0]/2, omega + k2[1]/2)
    k4 = dt*f(phi1+k3[0], omega + k3[1])
    
    phi1 +=(k1[0] + 2*k2[0] +2*k3[0] + k4[0])/6
    omega +=(k1[1]+ 2*k2[1] +2*k3[1] + k4[1])/6
    
    Approx = phi1list[0] * np.cos(np.sqrt(g1/R1) * t)
 
    Approxlist.append(Approx)
    
    t +=dt
    tlist.append(t)
    phi1list.append(phi1)
    omegalist.append(omega)
   


    
    
plt.figure()
plt.plot(tlist,np.degrees(phi1list),color = 'r' , label = "ODE Solver")
plt.xlabel("time(s)")
plt.ylabel('phi(degrees)' )

plt.plot(tlist,np.degrees(Approxlist), color = 'b', label = "Approxamite")
plt.title(" ODE Solver vs Approxamite Solution for phi0 = 20 degrees")
plt.legend()
plt.grid(True)
plt.show()




#=============================PLOT=====================================

