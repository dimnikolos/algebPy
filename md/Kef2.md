# Η έννοια του κλάσματος
> Ένα βράδυ τρεις φίλοι αγοράζουν μια πίτσα και την χωρίζουν σε οκτώ κομμάτια. Ο ένας έφαγε το ένα, ο δεύτερος τα τρία και ο τρίτος δύο κομμάτια από αυτά που περίσσεψαν.
> 1. Μπορείς να βρεις το μέρος της πίτσας που έφαγε ο καθένας;
> 2. Τι μέρος της πίτσας περίσσεψε;

Ο πρώτος έφαγε το $\frac{1}{8}$ ο δεύτερος τα $\frac{3}{8}$ και ο τρίτος τα \frac{2}{8}.
Επομένως και οι τρεις μαζί έφαγαν $1+3+2=6$ κομμάτια, δηλαδή τα $\frac{6}{8} της πίτσας. Άρα περίσσεψαν τα υπόλοιπα δύο κομμάτια από τα οκτώ, δηλαδή τα \frac{2}{8} της πίτσας.

Πώς μπορούν να γίνουν πράξεις με κλάσματα στην python; Με τις γνώσεις που ήδη έχουμε εκτελούμε τις παρακάτω εντολές:
```python
>>> 1/8
0.125
>>> 3/8
0.375
>>> 2/8
0.25
```
Θυμηθείτε ότι η python χρησιμοποιεί την τελεία για τους δεκαδικούς!
Τι μέρος της πίτσας περίσσεωε;
```python
>>> 1 - 1/8 - 3/8 - 2/8
0.25
```

Όμως, υπάρχει τρόπος η python να υπολογίζει κλάσματα. Απλά θα πρέπει να εισαχθεί το κατάλληλο module. Στην python υπάρχει διαθέσιμο τέτοιο module και ονομάζεται fractions. Για το δεύτερο ερώτημα λοιπόν μπορούμε να κάνουμε το εξής:
```
>>> import fractions
>>> prwtos = fractions.Fraction(1,8)
>>> deuteros = fractions.Fraction(3,8)
>>> tritos = fractions.Fraction(2,8)
>>> 1 - prwtos - deuteros - tritos
Fraction(1, 4)
```
Έτσι η python υπολογίζει το αποτέλεσμα με τη μορφή κλάσματος και Fraction(1,4) σημαίνει $\frac{1}{4}$.

Παρατηρείτε ότι γράφουμε το όνομα του module στη συνέχεια την τελεία "." και τέλος το Fraction. Με αυτόν τον τρόπο καλούμε κάτι που υπάρχει μέσα στο module. Υπάρχει όμως και ένας πιο εύκολος τρόπος για να εισάγουμε μόνο τις λειτουργίες που θέλουμε από ένα module και να τις καλούμε.
```python
>>> from fractions import Fraction
>>> prwtos = Fraction(1,8)
>>> deuteros = Fraction(3,8)
>>> tritos = Fraction(2,8)
>>> 1 - prwtos - deuteros - tritos
Fraction(1, 4)
```
Χρειάζεται προσοχή μόνο αν υπάρχουν περισσότερα από ένα module που πιθανόν να έχουν την ίδια λειτουργία κάτι που δεν ισχύει σε αυτήν την περίπτωση. 

> Μια σοκολάτα ζυγίζει 120 gr και έχει 6 ίσα κομμάτια.
> (α)   Ποιο μέρος της σοκολάτας είναι το κάθε κομμάτι;
> (β)   Πόσα κομμάτια πρέπει να κόψουμε για να πάρουμε 40 gr;

Το μέρος της σοκολάτας είναι $\frac{1}{6}$ για να βρούμε πόσα κομμάτια χρειαζόμαστε για 40gr θα πρέπει να βρούμε το βάρος του κομματιού που είναι $\frac{1}{6}\cdot 120$. Τέλος, τα κομμάτια που πρέπει να κόψουμε προκύπτουν από τη διαίρεση των 40 γραμμαρίων με το βάρος του κάθε κομματιού.

```python
from fractions import Fraction

sok = Fraction(1,6)
print(sok)
baroskommatiou = sok * 120
kommatia = 40 / baroskommatiou
print('Θα κόψω ' + str(kommatia) + ' κομμάτια!')
```
το αποτέλεσμα θα είναι το εξής:
```python
1/6
Θα κόψω 2 κομμάτια!
```

> Το καμπαναριό μιας εκκλησίας έχει ύψος 20 m, ενώ η εκκλησία έχει ύψος τα Εικόνα του ύψους του καμπαναριού. Ποιο είναι το ύψος της εκκλησίας;
```python
from fractions import Fraction

>>> kampanario = Fraction(3,5)*20
>>> print(kampanario)
12
```
Άρα το ύψος της εκκλησίας είναι 12m.

Στη συνέχεια η εντολή from fractions import Fraction θα υποννοείται ώστε να μην επαναλαμβάνεται συνεχώς. Αν τυχόν την ξεχάσετε το αποτέλεσμα θα έχει το εξής σφάλμα:
```python
NameError: name 'Fraction' is not defined
```
> Μια δεξαμενή πετρελαίου σε μια πολυκατοικία, χωράει 2000 lt. Ο διαχειριστής σε μια μέτρηση βρήκε ότι ήταν γεμάτη κατά τα Εικόνα. Πόσα λίτρα πετρέλαιο είχε η δεξαμενή;

```python
>>> dexameni = Fraction(3,4)*2000
>>> print(dexameni)
1500
```

Η δεξαμενή έχει 1500 lt.

>  	Τα $\frac{3}{5}$ του κιλού τυρί κοστίζουν 27 €. Πόσο κοστίζουν τα $\frac{8}{9}$ του κιλού;

```python
>>> enaPempto = Fraction(27,3)
>>> tyri = 5*enaPempto
>>> oktwEnata = Fraction(8,9)*tyri
>>> print(oktwEnata)
40
```
Τα \frac{8}{9} του τυριού κοστίζουν 40 ευρώ.
## Άσκήσεις
> Είναι τα κλάσματα $\frac{3}{4}$, $\frac{2}{3}$, $\frac{7}{9}$, $\frac{10}{9}$, $\frac{18}{20}$ όλα μικρότερα της μονάδας:

```python
>>> print(Fraction(3,4)<1)
True
>>> print(Fraction(2,3)<1)
True
>>> print(Fraction(7,9)<1)
True
>>> print(Fraction(10,9)<1)
False
>>> print(Fraction(18,20)<1)
True
```

> Τι κλάσμα των μαθητών της τάξης 28 μαθητών είναι οι 4 απόντες;

```python
>>> print(Fraction(4,28))
1/7
```

Παρατηρούμε ότι η εντολή Fraction(4,28) κάνει απλοποίηση κλάσματος.

> Αν το Εικόνα ενός κιλού καρύδια είναι 14 καρύδια, το κιλό περιέχει 70 καρύδια;
```python
>>> print(14*5 == 70)
```
Ναι.

> Βρες ποιο μέρος του κιλού είναι τα: (α) 100, (β) 250, (γ) 500, (δ) 600 γραμμάρια.

```python
>>> print(Fraction(100,1000))
1/10
>>> print(Fraction(250,1000))
1/4
>>> print(Fraction(500,1000))
1/2
>>> print(Fraction(600,1000)).
3/5
```
> Ποιο μέρος: (α) του μήνα, (β) του εξαμήνου, (γ) του έτους είναι οι 15 ημέρες;

```python
>>> print(Fraction(15,30))
1/2
>>> print(Fraction(15,180))
1/12
>>> print(Fraction(15,365))
3/73
```

> Ένα κατάστημα κάνει έκπτωση στα είδη του ίση με τα $\frac{2}{5}$ της αρχικής τιμής τους. Ένα φόρεμα κόστιζε 90 € πριν την έκπτωση. Υπολόγισε πόσα ευρώ έκπτωση έγινε στο φόρεμα και πόσο θα πληρώσουμε για να το αγοράσουμε.

```python
>>> ekpt = Fraction(2,5)*90
>>> print("Η έκπτωση είναι: " + str(ekpt) + " ευρώ!")
Η έκπτωση είναι: 36 ευρώ!
>>> plir = 90 - ekpt
>>> print("Θα πληρώσουμε: " + str(plir) + " ευρώ!")
Θα πληρώσουμε: 54 ευρώ!
```

> Σε μία τάξη τα $\frac{3}{8}$ των μαθητών μαθαίνουν αγγλικά. Να βρεις πόσους μαθητές έχει η τάξη, αν γνωρίζεις ότι αυτοί που μαθαίνουν αγγλικά είναι 12 μαθητές.

```python
>>> print(Fraction(8,3)*12)
32
```

> Σε ένα ορθογώνιο παραλληλόγραμμο η μια πλευρά του είναι 33 εκατοστά και η άλλη τα Εικόνα της πρώτης. Να βρεις την περίμετρο του ορθογωνίου.

```python
>>> plevra1 = 33
>>> plevra2 = Fraction(3,11)*plevra1
>>> perimetros = 2*(plevra1 + plevra2)
>>> print(perimetros)
84
```

```
# Ισοδύναμα κλάσματα

> Να εξετάσετε αν τα κλάσματα: α) $\frac{3}{5}$ και $\frac{10}{14}$ β) $\frac{3}{8}$ και $\frac{18}{48}$ είναι ισοδύναμα.

```python
print(Fraction(3,5) == Fraction(10,14))
False
print(Fraction(3,8) == Fraction(18,48))
True
```

Έτσι, τα $\frac{3}{5}$ και $\frac{10}{14}$ δεν είναι ισοδύναμα ενώ τα $\frac{3}{8}$ και $\frac{18}{48}$ είναι.

> Να απλοποιηθεί το κλάσμα $\frac{30}{66}$

```python
>>> print(Fraction(30,66))
5/11
```

```
#ask3 
def tiposemeparonomasti(k,p):
  if p % k.denominator == 0:
    coef = int(p // k.denominator)
    print(str(k.numerator * coef) + '/' + str(k.denominator * coef))
  else:
    print(k)

def ekp(a,b):
  return(a*b/gcd(a,b))
a = Fraction(3,5)
b = Fraction(2,3)
c = Fraction(5,20)
    
koinos = ekp(a.denominator,ekp(b.denominator,c.denominator))
tiposemeparonomasti(a,koinos)
tiposemeparonomasti(b,koinos)
tiposemeparonomasti(c,koinos)

print(Fraction(2,3)==Fraction(18,27))
print(Fraction(3,4)==Fraction(1,2))
print(Fraction(7,8)==Fraction(30,40))
print(Fraction(13,14)==Fraction(26,28))

tiposemeparonomasti(Fraction(3,4),100)
tiposemeparonomasti(Fraction(8,5),100)
tiposemeparonomasti(Fraction(4,20),100)
tiposemeparonomasti(Fraction(5,2),100)
tiposemeparonomasti(Fraction(60,75),100)

print(Fraction(10,6))
print(Fraction(50,30))
print(Fraction(18,27))

tiposemeparonomasti(Fraction(2,3),6)
tiposemeparonomasti(Fraction(2,3),15)

print(Fraction(25,30))
print(Fraction(12,9))
print(Fraction(32,56))

"""
#----------------------------------------------------
"""
print(Fraction(1,4)+Fraction(2,4) + 3)

print(Fraction(3,12) + Fraction(7,20))
print(Fraction(3,12) - Fraction(7,20))

print(1-Fraction(1,2) - Fraction(1,3))

def tiposemikto(k):
  if k.numerator > k.denominator:
    akeraios = (k.numerator - k.numerator % k.denominator) // k.denominator
    klasma = Fraction(k.numerator % k.denominator, k.denominator)
    print(str(akeraios) + " " + str(klasma))
  else:
    print(k)
    
tiposemikto(Fraction(15,4))
tiposemikto(Fraction(5,2))
tiposemikto(Fraction(38,12))

print(Fraction(5,9) - Fraction(3,8))

print(1-Fraction(2,5) - Fraction(2,15) - Fraction(1,3) - Fraction(1,10))
"""
#----------------------------------------------------
"""
print(Fraction(3,7)*Fraction(70,6)*Fraction(8,5))

print((Fraction(7,3) + Fraction(2,15)) * Fraction(3,8))

print(Fraction(2,3)/Fraction(10,9))
"""
#----------------------------------------------------
print(max(Fraction(7,15),Fraction(7,10)))
print(max(Fraction(5,8),Fraction(4,9)))
print(sorted([Fraction(5,3),Fraction(7,2),Fraction(8,9),Fraction(63,5),Fraction(125,10)]))

print(Fraction(1,4)+Fraction(2,4)+3)
print(Fraction(3,12)+Fraction(7,20))
print(Fraction(3,12)-Fraction(7,20))
print(Fraction(15,4)-1)
print(2+1+Fraction(1,3))
```python
