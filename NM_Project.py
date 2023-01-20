import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

window = Tk()

def solvingODEmain():
    def solvingODE(x0, y0, xn, n, f):
        def function(x, y):
            return eval(f)
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
        euler(x0, y0, xn, n)
        rk2(x0, y0, xn, n)
        rk4(x0, y0, xn, n)
        plt.legend(loc="upper left")
        plt.grid()
        plt.axhline(y=0)
        plt.axvline(x=0)
        plt.show()
   
    def solvingODEplacedata():
        x0 = x0lbl.get()
        y0 = y0lbl.get()
        xn = xnlbl.get()
        n = nlbl.get()
        function = func.get()
        solvingODE(float(x0), float(y0), float(xn), int(n), function)
    solvingODEwindow = Toplevel(window)
    solvingODEframe = Frame(solvingODEwindow)
    solvingODEframe.pack(side = TOP, pady=50)
    title = Label(solvingODEframe, text="Solving first order ordinary differential equation", font=('Arial', 25))
    title.pack()
    solvingODEwindow.geometry("800x800+560+140")
    x0text = Label(solvingODEwindow, text="x0 =", font=('Arial', 10))
    x0text.place(x=45, y=148)
    x0lbl = Entry(solvingODEwindow, width=45) 
    x0lbl.place(x=80, y=150)
    y0text = Label(solvingODEwindow, text="y0 =", font=('Arial', 10))
    y0text.place(x=45, y=198)
    y0lbl = Entry(solvingODEwindow, width=45) 
    y0lbl.place(x=80, y=200)
    xntext = Label(solvingODEwindow, text="xn =", font=('Arial', 10))
    xntext.place(x=45, y=248)
    xnlbl = Entry(solvingODEwindow, width=45) 
    xnlbl.place(x=80, y=250)
    ntext = Label(solvingODEwindow, text="n =", font=('Arial', 10))
    ntext.place(x=52, y=298)
    nlbl = Entry(solvingODEwindow, width=45) 
    nlbl.place(x=80, y=300)
    functext = Label(solvingODEwindow, text="dy/dx =", font=('Arial', 10))
    functext.place(x=27, y=348)
    func = Entry(solvingODEwindow, width=45) 
    func.place(x=80, y=350)
    btn2 = Button(solvingODEwindow, text="Submit", fg="black", command = solvingODEplacedata)
    btn2.place(x=80, y=400)

def solvingNonLinearEqnMain():
    
    def secant(x0, x1, function, steps, tol_error):
        def showGraph():
            x = np.linspace(-5, 5, 50)
            plt.plot(x, eval(function), label="Graph of function")
            plt.grid()
            plt.axhline(y=0)
            plt.axvline(x=0)
            plt.show()
        def f(x):
            return eval(function)
        count = 1
        e = tol_error
        condition = True
        ZeroDeno = False
        NoConverge = False
        max_steps=steps
        while condition:
            if f(x0) == f(x1): 
                print("Zero Denominator\n")
                ZeroDeno = True
                break 
            x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
            x0 = x1
            x1 = x2 
            count += 1
            if count > max_steps:
                print("Does not converge\n")
                NoConverge = True
                break 
            condition = abs(f(x2)) > e 
        if ZeroDeno:
            outputText = Label(solvingNonLinearEqnWindow, text="The x-value has zero denominator!", font=('Arial', 15), justify=CENTER).place(x=80, y=450)
        elif NoConverge:
            outputText = Label(solvingNonLinearEqnWindow, text="The x-value does not converge!", font=('Arial', 15), justify=CENTER).place(x=80, y=450)
        else:
            outputText = Label(solvingNonLinearEqnWindow, text="The root of the function = " + str(x2), font=('Arial', 15), justify=CENTER).place(x=80, y=450)
        graphbtn = Button(solvingNonLinearEqnWindow, text="Show Graph", fg="black", command=showGraph).place(x=80, y=490)

    def placeData():
        x1 = x1lbl.get()
        x2 = x2lbl.get() 
        func = flbl.get()
        steps = nlbl.get()
        tol_error = elbl.get()
        secant(float(x1), float(x2), func, int(steps), float(tol_error))

    solvingNonLinearEqnWindow = Toplevel(window)
    solvingNonLinearEqnWindow.geometry("800x800+560+140")
    solvingNonLinearEqnFrame = Frame(solvingNonLinearEqnWindow)
    solvingNonLinearEqnFrame.pack(side = TOP, pady = 50)
    title = Label(solvingNonLinearEqnFrame, text="Solving Non Linear Equations", font = ('Arial', 25))
    title.pack()
    x1text = Label(solvingNonLinearEqnWindow, text="x1 =", font=('Arial', 10))
    x1text.place(x=45, y=148)
    x1lbl = Entry(solvingNonLinearEqnWindow, width=45) 
    x1lbl.place(x=80, y=150)
    x2text = Label(solvingNonLinearEqnWindow, text="y0 =", font=('Arial', 10))
    x2text.place(x=45, y=198)
    x2lbl = Entry(solvingNonLinearEqnWindow, width=45) 
    x2lbl.place(x=80, y=200)
    ftext = Label(solvingNonLinearEqnWindow, text="f(x) =", font=('Arial', 10))
    ftext.place(x=42, y=248)
    flbl = Entry(solvingNonLinearEqnWindow, width=45) 
    flbl.place(x=80, y=250)
    ntext = Label(solvingNonLinearEqnWindow, text="n =", font=('Arial', 10))
    ntext.place(x=52, y=298)
    nlbl = Entry(solvingNonLinearEqnWindow, width=45) 
    nlbl.place(x=80, y=300)
    etext = Label(solvingNonLinearEqnWindow, text="e =", font=('Arial', 10))
    etext.place(x=52, y=348)
    elbl = Entry(solvingNonLinearEqnWindow, width=45) 
    elbl.place(x=80, y=350)
    btn = Button(solvingNonLinearEqnWindow, text="Submit for Secant Method", fg="black", command = placeData)
    btn.place(x=80, y=400)

         
window.title('Numerical Methods')
maintitleframe = Frame(window)
maintitleframe.pack(side=TOP, pady=50)
maintitletext = Label(maintitleframe, text="Numerical Methods - SH553", font=('Arial', 25))
maintitletext.pack()
window.geometry("800x800+560+140")
btn1 = Button(window, text="Solving first order ODE", fg="black", command = solvingODEmain, font=('Arial',12), width=60)
btn1.pack()
btn2 = Button(window, text="Solution of Non-Linear Equations", fg="black", command = solvingNonLinearEqnMain, font=('Arial',12), width=60)
btn2.pack()
window.mainloop()

