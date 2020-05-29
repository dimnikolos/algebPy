def frommmto(num,mon):
    if mon == 'mm':
        return(num)
    elif mon=='cm':
        return(num/10)
    elif mon=='dm':
        return(num/100)
    elif mon=='m':
        return(num/1000)
    elif mon=='Km':
        return(num/1000000)
    else:
        return(None)
def tommfrom(num,mon):
    if mon == 'mm':
        return(num)
    elif mon=='cm':
        return(num*10)
    elif mon=='dm':
        return(num*100)
    elif mon=='m':
        return(num*1000)
    elif mon=='Km':
        return(num*1000000)
    else:
        return(None)

def changeUnit(num,arx_mon,tel_mon):
    mms = tommfrom(num,arx_mon)
    if mms is not None:
        result = frommmto(mms,tel_mon)
        return(result)
    else:
        return(None)

print(changeUnit(23,'dm','cm'))
print(changeUnit(3.1,'m','Km'))
print(changeUnit(45.83,'cm','m'))
print(changeUnit(67.2,'Km','mm'))
print(changeUnit(95.5,'mm','cm'))