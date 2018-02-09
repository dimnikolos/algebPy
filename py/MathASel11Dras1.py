"""
Μαθηματικά Α΄ Γυμνασίου

Σελίδα 11

Διάλεξε έναν τριψήφιο αριθμό. Βρες όλους τους διαφορετικούς τριψήφιους αριθμούς που προκύπτουν όταν εναλλάξεις τα ψηφία του αριθμού που διάλεξες και γράψε αυτούς με όλους τους δυνατούς τρόπους. 
+ Ποιος είναι ο μικρότερος και ποιος ο μεγαλύτερος; 
+ Γράψε όλους τους αριθμούς που βρήκες με σειρά αύξουσα, δηλαδή από το μικρότερο προς το μεγαλύτερο. 
+ Στη συνέχεια, γράψε τους ίδιους αριθμούς με φθίνουσα σειρά.
"""

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
    for arithmos in sorted(enallages,reverse = True):
        print(arithmos)
else:
    print('Δεν δώσατε τριψήφιο αριθμό')

