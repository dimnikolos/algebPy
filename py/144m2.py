import matplotlib.pyplot as plt
from numpy import arange

plt.clf()
x = arange(1,20,0.5)
y = [144/p for p in x]
perimetros = [2*p+2*144/p for p in x]
plt.grid()
plt.scatter(x,y, s=100 ,marker='.', c='m')
plt.scatter(x,perimetros,s=100,marker='.',c='r')
plt.show()