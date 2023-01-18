import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def function(x, y):
    return x+y

def euler(x0, y0, xn, n):
    h = (xn - x0)/n 
    xvalues = []
    yvalues = []
    for i in range(n):
        yn = y0 + h*function(x0, y0) 
        y0 = yn 
        x0 = x0 + h
        xvalues.append(x0)
        yvalues.append(y0)
    plt.plot(xvalues, yvalues, label = "Euler")

def rk2(x0, y0, xn, n):
    h = (xn - x0)/n 
    xvalues = [] 
    yvalues = [] 
    for i in range(n):
        k1 = h*function(x0, y0) 
        k2 = h*function(x0 + h, y0 + k1) 
        k = (k1 + k2)/2 
        y0 += k
        x0 += h 
        xvalues.append(x0)
        yvalues.append(y0)
    plt.plot(xvalues, yvalues, label = "RK2")

def rk4(x0, y0, xn, n):
    h = (xn - x0)/n 
    xvalues = [] 
    yvalues = []
    for i in range(n):
        k1 = h*function(x0, y0) 
        k2 = h*function(x0+h/2, y0+k1/2) 
        k3 = h*function(x0+h/2, y0+k2/2) 
        k4 = h*function(x0+h, y0+k3) 
        k = (k1 + 2*k2 + 2*k3 +k4)/6
        y0 += k
        x0 += h 
        xvalues.append(x0)
        yvalues.append(y0)
    plt.plot(xvalues, yvalues, label = "RK4")

x0 = float(input("Enter starting x coordinate: "))
y0 = float(input("Enter starting y coordinate: "))
xn = float(input("Ending x coordinate: "))
n = int(input("Number of steps: "))
euler(x0, y0, xn, n)
rk2(x0, y0, xn, n)
rk4(x0, y0, xn, n)
plt.legend(loc="upper left")
plt.show()

