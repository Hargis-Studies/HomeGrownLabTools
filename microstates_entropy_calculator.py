# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:04:43 2025

@author: Hargi
"""

from math import factorial

E_total = 120
NA = NB = 40  


omega_total = 0


for E_A in range(E_total + 1): 
 
    omega_A = factorial(NA + E_A - 1) / (factorial(E_A) * factorial(NA - 1))

   
    E_B = E_total - E_A
    omega_B = factorial(NB + E_B - 1) / (factorial(E_B) * factorial(NB - 1))

    
    omega_total += omega_A * omega_B


print("Total number of accessible microstates:", omega_total)


from math import log
entropy = log(omega_total)
print("Total entropy:", entropy)
