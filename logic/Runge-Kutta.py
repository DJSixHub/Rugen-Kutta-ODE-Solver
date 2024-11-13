import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def runge_kutta(x0,y0,h,fun,title):
    def _runge_kutta(f,y0,x_span,h,fun):

        t = np.arange(x_span[0],x_span[1] + h,h)
        y = np.zeros(len(t))
        y[0] = y0

        for i in range(len(t)-1):
            k1 = h * f(t[i],y[i],fun)
            k2 = h * f(t[i] + h/2,y[i] + k1/2,fun)
            k3 = h * f(t[i] + h/2,y[i] + k2/2,fun)
            k4 = h * f(t[i] + h/2,y[i] + k3,fun)
            y[i+1] = y[i]+(1/6*k1 + 1/3*k2 + 1/3*k3 + 1/6*k4)

        return t,y

    def f(x,y,fun):
        return fun(x,y)
        
    x0 = x0
    y0 = y0
    x_span = (x0,10)
    h = h
    t,y_r = _runge_kutta(f,y0,x_span,h,fun)
    return t,y_r,sol.t,sol.y[0]

def f(x,y):
    return x+y

runge_kutta(0, 0, 0.6,f,'x+y')

