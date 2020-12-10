# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:39:44 2020

@author: ARCHISMAN ROY
"""

List1 = ["Madrid","Barcelona","Bayern","Monaco","Atletico","Chelsea","Man Utd",
         "Paris","City"]
print(List1)
x= input("Enter a starting letter :")
y=str(x)
for s in List1:
    if s.startswith(y):
        print(s)