def zygisi(barosKila,barosg,stathmaseg):
    baros = barosKila * 1000 + barosg
    stathmos = 0
    res = [0]*len(stathmaseg)
    s = list(stathmaseg)
    while baros>=min(s):
        if baros >= max(s):
            res[stathmaseg.index(max(s))]=baros//max(s)
            baros = baros % max(s)
        s.pop(s.index(max(s)))
        if not s:
            break
    return(res)

print(zygisi(3,600,[1000,50,500]))
print(zygisi(2,450,[50,500,1000]))