from astAL import Expression
from lexer import Lexer, TOKEN_PATTERNS, CONSTANTS, Token
from parser import Parser
import numpy as np
import matplotlib.pyplot as plt


lexer = Lexer(TOKEN_PATTERNS, CONSTANTS)
tokens: list[Token] = lexer.tokenize(function)
parser = Parser()
ast: Expression = parser.make_ast(tokens)
print(ast)


def edo(ast: Expression, vars: dict):
    variables = {"e": 2.718281828459045, "pi": 3.14}
    for key, value in vars.items():
        variables[key] = value
    return ast.eval(variables)



def RungeKutta(x_point, y_point, h):
    
    X = np.arange(0,5,h)
    y = np.zeros(len(X))
    y[0]=y_point

    #### Runge-Kutta 
    for i in range(len(X)-1): 
        k1 =  edo(ast,{'x': i, 'y': y[i]})
        k2 =  edo(ast,{'x': i + h / 2, 'y': y[i] + k1 / 2})
        k3 =  edo(ast,{'x': i + h / 2, 'y': y[i] + k2 / 2})
        k4 =  edo(ast,{'x': i + h, 'y': y[i] + k3})
        y[i+1] = (y[i] + h*(1/6 * k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4))
   
    return X,y


RungeKutta(x_point,y_point,h)



