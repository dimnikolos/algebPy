from sympy import *
x = symbols('x')
pointsList = [[(4,10),(7,17.5),(12,30)],
              [(5,11),(7.5,16),(9,19)],
              [(2,7),(3,9),(10,23)],
              [(2,6),(4,3),(6,2)],
              [(2,1),(5,2.5),(0.5,0.25)],
              [(0.2,2.4),(6,14),(10,22)],
              [(1,3),(1.2,3.6),(2.5,7.5)],
              [(0.8,2.2),(1,3),(1.5,5)]]

typoi = [2*x+3,3*x,12/x,2.5*x,2*x+2,2*x+1,4*x-1,0.5*x]
onomataPinaka = ['Α','Β','Γ','Δ','Ε','Ζ','Η','Θ']

for (arithmosPinaka,points) in enumerate(pointsList):
    for (arithmosTipou, t) in enumerate(typoi):
        for p in points:
            x = symbols('x')
            if abs((p[1] - t.subs(x,p[0]))) > 1e-8:
                break
        else:
            print(onomataPinaka[arithmosPinaka],'-',arithmosTipou+1)