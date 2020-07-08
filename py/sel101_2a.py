import matplotlib.pyplot as plt
from sympy import *

points = [(0,0),(10,0.01*10)]
x = [p[0] for p in points]
y = [p[1] for p in points]
plt.grid()
plt.plot(x,y, marker='o', c='m')

plt.show()