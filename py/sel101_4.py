import matplotlib.pyplot as plt

plt.clf()
pointslist = [[(0,0),(5000,5000/40)],
                        [(0,0),(5000,5000/20)],
                        [(0,0),(5000,5000/50)]]
colors = ['r','g','b']
for (i,points) in enumerate(pointslist):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.grid(b=True, which='minor')
    plt.grid(b=True, which='major')
    plt.xlim(0,5000)
    plt.ylim(0,210)
    plt.minorticks_on()
    plt.plot(x,y, marker='o', c=colors[i])

plt.plot([4000,4000,0],[0,80,80],c='k')
plt.plot([4000,4000,0],[0,100,100],c='k')
plt.plot([4000,4000,0],[0,200,200],c='k')
plt.show()