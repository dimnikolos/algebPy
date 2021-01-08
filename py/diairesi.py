def diairesi(D,d):
    if (type(D)!=int ) or (type(d)!=int):
        print('Η διαίρεση της βιβλιοθήκης υποστηρίζει μόνο ακέραιους!')
        return(None)
    pad = len(str(D))+1
    print(str(D).rjust(pad)+'|'+str(d))
    i = 1
    while int(str(D)[0:i])<d:
        i += 1
    p = int(str(D)[0:i])//d
    y = int(str(D)[0:i])%d
    print(('-'+str(p*d)).ljust(pad)+'|'+str(D//d))
    print('-'*pad+'|')
    while i < len(str(D)):
        print((str(str(y)+str(D)[i])).rjust(i+2).ljust(pad)+'|')
        neoD = int(str(y)+str(D)[i])
        p = neoD//d
        print(('-'+str(p*d)).rjust(i+2).ljust(pad)+'|')
        print('-'*pad+'|')
        y = neoD%d
        i+=1
    print((str(y)).rjust(i+1).ljust(pad)+'|')
        
        
        
    
    
    
diairesi(13,3)    
diairesi(1578,32)
