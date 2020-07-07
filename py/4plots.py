import matplotlib.pyplot as plt

plt.clf()
pointsA = [(0,0),(1,2),(2,1),(3,1.5)]
pointsB = [(0,1),(1,1.5),(2,2),(3,2.5)]
pointsC = [(0,0),(1,1),(2,2),(3,3)]
pointsD = [(0,0),(1,0.5),(2,1),(3,1.5)]

x = [p[0] for p in pointsA]
y = [p[1] for p in pointsA]
plt.grid()
plt.plot(x,y, marker='o', c='r')


x = [p[0] for p in pointsB]
y = [p[1] for p in pointsB]
plt.grid()
plt.plot(x,y, marker='o', c='g')


x = [p[0] for p in pointsC]
y = [p[1] for p in pointsC]
plt.grid()
plt.plot(x,y,marker='o', c='b')


x = [p[0] for p in pointsD]
y = [p[1] for p in pointsD]
plt.grid()
plt.plot(x,y, marker='o', c='m')
plt.show()