import matplotlib.pyplot as plt

plt.clf()
pointslist = [[(0,0),(1,2),(2,1),(3,1.5)],
          [(0,1),(1,1.5),(2,2),(3,2.5)],
          [(0,0),(1,1),(2,2),(3,3)],
          [(0,0),(1,0.5),(2,1),(3,1.5)]]
colors = ['r','g','b','m']
for (i,points) in enumerate(pointslist):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.grid()
    plt.plot(x,y, marker='o', c=colors[i])

plt.show()