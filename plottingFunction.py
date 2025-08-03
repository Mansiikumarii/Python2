import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.show()  # <-- Add this to display the plot

# Define the vectors
u = np.array([1, 0])
v = np.array([0, 1])
z = np.array([1, 1])

Plotvec1(u, z, v)