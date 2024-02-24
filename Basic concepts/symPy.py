#symPy module
#-------------------------

from sympy import *
x ,y =symbols('x y')
equ = 2 * x +y
print(equ) #2*x + y
equ *=equ
print(equ) #(2*x + y)**2

x = symbols('x')
equ = x +1
x = 2
print(equ) #x + 1
x = symbols('x')
equ = x +1
result = equ .subs(x,2)
print(result) #3

