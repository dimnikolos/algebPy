from sympy import *
x,y,w,a,b  = symbols('x y w a b')
s = [x,y,w,a,b]
e = [x-2,1+y,18-w,2-a,93-b]
res = [4,4,10,1,86]
for (en,expr) in enumerate(e):
    for i in range(9):
        if expr.subs(s[en],i) == res[en]:
            print('X',end='')
        else:
            print('O',end='')
    print()