# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:59:02 2020

@author: ARCHISMAN ROY
"""

stack = []
x=input("Enter number of elements you want to input :" )
i=int(x)
k=0
while k<i:
    stack.append(input("Enter element :"))
    k=k+1
print("The final stack :",stack)
