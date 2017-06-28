# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:34:41 2017

@author: moazi
"""

import numpy as np
import scipy.optimize as opt

# simplex algorithm finds min of a LP programing consraint
ingredients = ['tomato', 'lettus', 'spinach', 'carrot', 'oil']
c = [21, 16, 371, 346, 884]  # min calories
# uA = upper bound (you can enter lower bound with inverse upper bound)
uA = np.array([[.33, .2, 1.58, 1.39, 100],  # fat
               [9, 8, 7, 508, 0],  # sodium
               [-1, 1, 1, -1, -1],  # greens
               [.33, .2, 1.58, 1.39, 100],  # fat
               [.85, 1.62, 12.78, 8.39, 0],  # protine
               [4.64, 2.37, 74.69, 80.7, 0]])  # card
# upper bound array -negitive lower bound = upper bound
b = np.array([6, 100, 0, -2, -15, -4])
uA = np.vstack((uA[:3], -1*uA[3:]))  # converting lowerbound quations to upper
res = opt.linprog(c, A_ub=uA, b_ub=b, options={"disp": True})
ingred_amnt = res['x']

print("Results:\n","total Calories: ", res['fun'])
for i, j in zip(ingredients, ingred_amnt):
    print(i, j)

#for i in res:
#    print(i)
"""
Results:
 total Calories:  232.514698996
tomato 5.88480149852
lettus 5.84317602373
spinach 0.0416254747906
carrot 0.0
oil 0.0
"""
"""
# Check for accuracy
uA = np.array([[.33,.2, 1.58, 1.39,100],#fat
               [9,8,7,508,0],#sodium
               [-1,1,1,-1,-1],#greens 
               [.33,.2, 1.58, 1.39,100],
               [.85,1.62,12.78,8.39,0],
               [4.64,2.37,74.69,80.7,0]])
x = np.array([ 5.8848015 ,  5.84317602,  0.04162547,  0.        ,  0.        ])
for i in uA:
    print(sum(i*x))
"""
