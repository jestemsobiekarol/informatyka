# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:35:47 2021

@author: karol
"""
import matplotlib.pyplot as plt
import numpy as np

print("podaj A")
A=float(input())

print("podaj d")
d=float(input())

print("podaj f")
f=float(input())

print("podaj tmax")
tmax=float(input())

t = np.arange(0.0, tmax, 1)
s = A*np.exp(-t/d) * np.sin(2*np.pi*f*t)

fig, ax = plt.subplots()
ax.plot(t, s)

t = np.arange(0.0, tmax, 1)
v = [2*np.pi*f * np.cos(2*np.pi*f*t)-(np.sin(2*np.pi*f*t)/d)] * A * np.exp(-t/d)

fig, ax = plt.subplots()
ax.plot(t, v)

x = np.arange(0.0, tmax, 1)
v=[2*np.pi*f * np.cos(2*np.pi*f*t)-(np.sin(2*np.pi*f*t)/d)] * A * np.exp(-t/d)

fig, ax = plt.subplots()
ax.plot(x, v)


plt.show()