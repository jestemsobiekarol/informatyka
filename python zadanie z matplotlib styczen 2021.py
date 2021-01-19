# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:25:40 2021

@author: karol
"""
import matplotlib.pyplot as pyplot

print("podaj A")
A=float(input())

print("podaj d")
d=float(input())

print("podaj f")
f=float(input())



x=['1','2','3','4','5']
y=['1','2','3','4','5']
 
𝑥(𝑡)=𝐴*exp(−𝑡*𝑑⁄)sin(2pi*𝑓*𝑡)


pyplot.plot(x,y)
pyplot.xlabel("t")
pyplot.ylabel("x(t)")
pyplot.show()