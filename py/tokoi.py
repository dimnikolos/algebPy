prokataboli = 50/100*1200+19/100*1200
ypoloipo = (1200+19/100*1200) - prokataboli
dosixwristokous = ypoloipo/6
plirwse = prokataboli
print('Προκαταβολη:',prokataboli)

for i in range(6):
    dosi = dosixwristokous + 3/100*ypoloipo
    plirwse += dosi
    ypoloipo = ypoloipo - dosixwristokous
    print('Δόση '+str(i)+': '+str(dosi))

print('Συνολικα:',plirwse)