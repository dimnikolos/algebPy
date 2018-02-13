import itertools

x = input('Διάλεξε έναν τριψήφιο αριθμό:')
x = int(x)
if x>=100 and x<=999:
    psifio0 = x%10
    x = x - psifio0
    x = x // 10
    psifio1 = x%10
    x = x - psifio1
    x = x // 10
    psifio2 = x
  
    enallages = []
    for enallagi in itertools.permutations([psifio0,psifio1,psifio2]):
        arithmos = 100*enallagi[2]+10*enallagi[1]+enallagi[0]
        if arithmos not in enallages:
            enallages.append(arithmos)
    print('Ο μεγαλύτερος αριθμός είναι: ' + str(max(enallages)))
    print('Ο μικρότερος αριθμός είναι: ' + str(min(enallages)))
    print('Όλοι οι αριθμοί με αύξουσα σειρά:')
    for arithmos in sorted(enallages):
        print(arithmos)
    print('Όλοι οι αριθμοί με φθίνουσα σειρά:')
    for arithmos in sorted(enallages,reverse = True):
        print(arithmos)
else:
    print('Δεν δώσατε τριψήφιο αριθμό')