# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:48:47 2020

@author: ARCHISMAN ROY
"""

n = [24,45,41,(14,28),36,52]
print(n)
count = 0
for i in n:
    if isinstance(i, tuple):
        break
    count=count+1
print("Number of elemnts before tuple :",count)