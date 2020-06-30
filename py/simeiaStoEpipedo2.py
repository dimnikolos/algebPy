import matplotlib.pyplot as plt

plt.clf()
points = [(2,1), (1,2), (2,3), (3,2)]
pointName = ['Α','Β','Γ','Δ']
x = [p[0] for p in points]
y = [p[1] for p in points]
color=['m','g','r','b']
plt.grid()
plt.scatter(x,y, s=100 ,marker='o', c=color)
for (i,p) in enumerate(points):
    plt.annotate(pointName[i],(p[0],p[1]))

x = [points[0][0],points[2][0]]
y = [points[0][1],points[2][1]]
plt.plot(x,y)
x = [points[1][0],points[3][0]]
y = [points[3][1],points[3][1]]
plt.plot(x,y)



plt.show()