import itertools

def tripsifios(x):
    if x>=100 and x<=999:
        psifia = [int(i) for i in str(x)]
    else:
    	return(None)
    enallages = []
    for enallagi in itertools.permutations(psifia):
        arithmos = 100*enallagi[2]+10*enallagi[1]+enallagi[0]
        if arithmos not in enallages:
            enallages.append(arithmos)
    print('Ο μεγαλύτερος αριθμός είναι: ')
    print(max(enallages))
    print('Ο μικρότερος αριθμός είναι:')
    print(min(enallages))
    print('Όλοι οι αριθμοί με αύξουσα σειρά:')
    for arithmos in sorted(enallages):
        print(arithmos)
    print('Όλοι οι αριθμοί με φθίνουσα σειρά:')
    for arithmos in sorted(enallages,reverse = True):
        print(arithmos)
    
eisodos = input("Δώσε τριψήφιο")
tripsifios(int(eisodos))
