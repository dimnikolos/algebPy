# Μαθηματικά Α΄ Γυμνασίου
## Μέρος Α - Κεφάλαιο 1ο - Φυσικοί Αριθμοί
Το βιβλίο μαθηματικών της Α΄ Γυμνασίου αρχίζει στη σελίδα 11 με το εξής πρόβλημα:

>Διάλεξε έναν τριψήφιο αριθμό.	Βρες όλους τους διαφορετικούς	τριψήφιους αριθμούς που	προκύπτουν	όταν εναλλάξεις	τα	ψηφία	του	αριθμού	που	διάλεξες	και	γράψε	αυτούς με	όλους	τους	δυνατούς	τρόπους. 
>+ Ποιος	είναι	ο	μικρότερος	και	ποιος	ο	μεγαλύτερος; 
>+ Γράψε	όλους	τους	αριθμούς	που	βρήκες	με	σειρά	αύξουσα,	δηλαδή	από	το	μικρότερο	προς	το	μεγαλύτερο. 
>+ Στη	συνέχεια,	γράψε	τους	ίδιους	αριθμούς	με	φθίνουσα	σειρά.

Η λύση του προβλήματος σε Python είναι η παρακάτω ([κατεβάστε τη](https://raw.githubusercontent.com/dimnikolos/algebPy/master/py/MathASel11Dras1.py)):

```python
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


```

Δεν χρειάζετε να καταλάβετε από τώρα το πρόγραμμα αυτό, θα μελετήσουμε τα στοιχεία του αργότερα.

Για να εκτελέσετε το πρόγραμμα αυτό θα πρέπει να έχετε εγκαταστήσει τη γλώσσα προγραμματισμού Python στον υπολογιστή σας και συγκεκριμένα την Python 3.

>>>*Εγκατάσταση Python*
>>>[Ιστότοπος της Python](https://www.python.org/)

Στη συνέχεια ανοίγετε ένα Powershell και γράφετε:
```shell
python MathASel11Dras1.py
```

Το αποτέλεσμα της εκτέλεσης θα είναι κάπως έτσι:
>>>Εικόνα;

