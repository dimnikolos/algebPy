def antistrofosanaloga(x,y):
    if len(x) != len(y):
        print('Τα δεδομένα δεν έχουν το ίδιο μέγεθος')
        return(None)
    ginomeno = x[0]*y[0]
    for i in range(len(x)):
        if x[i]*y[i]!=ginomeno:
            return(False)
    return(True)

print(antistrofosanaloga([1,2,3,4],[2,1,2/3,1/2]))
print(antistrofosanaloga([0.25,0.4,0.5],[10,6.25,5]))
print(antistrofosanaloga([1/100,2/58,7/10,4],[100,29,10/7,1/4]))
print(antistrofosanaloga([3,6,9],[9,5,3]))