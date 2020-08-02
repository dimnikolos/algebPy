posotita = 3600/4
x = [20,15,10,5]
y = []
for doxeio in x:
    plithos = posotita / doxeio
    y.append(plithos)

kostos = [0.4,0.3,0.2,0.1]
synolikoKostos = 0
for (i,p) in enumerate(y):
    synolikoKostos += kostos[i]*p

print(y)
print(synolikoKostos)