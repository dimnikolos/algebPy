import matplotlib.pyplot as plt

plt.clf()
points = [(1,1), (2,2), (5,5), (10,10), (15,15)]
pointName = ['Α','Β','Γ','Δ','Ε']
x = [p[0] for p in points]
y = [p[1] for p in points]
color=['m','g','r','b']
plt.grid()
plt.scatter(x,y, s=100 ,marker='o', c=color)
for (i,p) in enumerate(points):
    plt.annotate(pointName[i],(p[0],p[1]))

plt.show()