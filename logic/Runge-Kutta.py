import numpy as np 
from scipy.integrate import solve_ivp
from typing import Callable

def runge_kutta(x0:float|int, y0:float|int, h:float, fun:Callable[int|float, int|float]):

    def _runge_kutta(f:Callable[int|float, int|float], y0:float|int,x_span, h:float|int, fun:Callable[int|float, int|float]):

        t = np.arange(x_span[0],x_span[1],h)
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
    #hay parametros tengo que ajustarlos para que coja más rango de valores
    sol = solve_ivp(fun, x_span, [y0], t_eval=np.linspace(x0, 10, 100))
 
    # los dos primeros son los calculados por nosotros, los otros dos son con el de python
    # las t son las x
    # y_r son las y
    return t,y_r,sol.t,sol.y[0]
   





"""
asi se llama 
def f(x,y):
    return x+y

runge_kutta(1,0,0.5,f)"""