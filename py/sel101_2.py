import matplotlib.pyplot as plt
from sympy import *
x = symbols('x')

analogies = [1/2*x,3*x,5.5*x,10*x,0.01*x]
colors = ['r','g','b','c','m']
for (i,s) in enumerate(analogies):
    x = symbols('x')
    points = [(0,0),(10,s.subs(x,10))]
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.grid()
    plt.plot(x,y, marker='o', c=colors[i])

plt.show()