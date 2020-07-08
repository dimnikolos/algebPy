import matplotlib.pyplot as plt

plt.clf()
points = [(0,0),(1,1.5),(2,3)]

x = [p[0] for p in points]
y = [p[1] for p in points]

plt.grid()
plt.plot(x,y, marker='o', c='r')

plt.show()