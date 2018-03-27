# Η έννοια του κλάσματος
> Ένα βράδυ τρεις φίλοι αγοράζουν μια πίτσα και την χωρίζουν σε οκτώ κομμάτια. Ο ένας έφαγε το ένα, ο δεύτερος τα τρία και ο τρίτος δύο κομμάτια από αυτά που περίσσεψαν.
> 1. Μπορείς να βρεις το μέρος της πίτσας που έφαγε ο καθένας;
> 2. Τι μέρος της πίτσας περίσσεψε;

Ο πρώτος έφαγε το $\frac{1}{8}$ ο δεύτερος τα $\frac{3}{8}$ και ο τρίτος τα $\frac{2}{8}$.
Επομένως και οι τρεις μαζί έφαγαν $1+3+2=6$ κομμάτια, δηλαδή τα $\frac{6}{8}$ της πίτσας. Άρα περίσσεψαν τα υπόλοιπα δύο κομμάτια από τα οκτώ, δηλαδή τα $\frac{2}{8}$ της πίτσας.

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
Τι μέρος της πίτσας περίσσεψε;
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
> Μια δεξαμενή πετρελαίου σε μια πολυκατοικία, χωράει 2000 lt. Ο διαχειριστής σε μια μέτρηση βρήκε ότι ήταν γεμάτη κατά τα $\frac{3}{4}$. Πόσα λίτρα πετρέλαιο είχε η δεξαμενή;

```python
>>> dexameni = Fraction(3,4)*2000
>>> print(dexameni)
1500
```

Η δεξαμενή έχει 1500 lt.

>  	Τα $\frac{3}{5}$ του κιλού τυρί κοστίζουν 27 €. 
>  	Πόσο κοστίζουν τα $\frac{8}{9}$ του κιλού;

```python
>>> enaPempto = Fraction(27,3)
>>> tyri = 5*enaPempto
>>> oktwEnata = Fraction(8,9)*tyri
>>> print(oktwEnata)
40
```
Τα $\frac{8}{9}$ του τυριού κοστίζουν 40 ευρώ.
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

> Αν το $\frac{1}{5}$ ενός κιλού καρύδια είναι 14 καρύδια, το κιλό περιέχει 70 καρύδια;
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

> Σε ένα ορθογώνιο παραλληλόγραμμο η μια πλευρά του είναι 33 εκατοστά και η άλλη τα $\frac{3}{11}$ της πρώτης. Να βρεις την περίμετρο του ορθογωνίου.

```python
>>> plevra1 = 33
>>> plevra2 = Fraction(3,11)*plevra1
>>> perimetros = 2*(plevra1 + plevra2)
>>> print(perimetros)
84
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

> Να μετατραπούν σε ομώνυμα τα κλάσματα $\frac{3}{5}$, $\frac{2}{3}$ και $\frac{5}{20}$:

Επειδή η Fraction κάνει απλοποίηση σε ανάγωγο κλάσμα δεν μπορούμε να επιλέξουμε παρονομαστή, γι' αυτό θα κατασκευάσετε μια συνάρτηση η οποία θα τυπώνει το κλάσμα επιλέγοντας τον παρονομαστή.

```python
def tiposemeparonomasti(k,p):
  """
  tiposemeparonomasti(k,p)
  Τύπωσε το κλάσμα k με παρονομαστή p
  """
  if p % k.denominator == 0:#αν το p είναι πολλαπλάσιο
                            #του τρέχοντος παρονομαστή (denominator)
                            #τότε μπορούμε να πολλαπλασιάσουμε
                            #όλο το κλάσμα με έναν συντελεστή
    synt = int(p // k.denominator)
    print(str(k.numerator * synt) + '/' + str(k.denominator * synt))
  else:#αν το p δεν είναι πολλαπλάσιο του τρέχοντος παρονομαστή
       #τότε τυπώνουμε το κλάσμα ως έχει
    print(k)
```

Το k.denominator είναι ο παρονομαστής του κλάσματος k.

Αφού φτιάξετε τη συνάρτηση tiposemeparonomasti δοκιμάστε:
```python
>>> tiposemeparonomasti(Fraction(3,4),12)
9/12
>>> tiposemeparonomasti(Fraction(1,2),20)
10/20
```

Για να κάνουμε ομώνυμα τα κλάσματα βρίσκουμε το Ελάχιστο Κοινό Πολλαπλάσιο (Ε.Κ.Π.) των παρονομαστών. 
Η συνάρτηση για το Ε.Κ.Π. είναι η παρακάτω, αφού το Ε.Κ.Π. δύο αριθμών προκύπτει από το γινόμενο τους αφού το διαιρέσουμε με τον μέγιστο κοινό διαιρέτη (Μ.Κ.Δ. - G.C.D.). Μάλιστα η βιβλιοθήκη fractions περιέχει τη συνάρτηση gcd που υπολογίζει το Μ.Κ.Δ. οπότε:
```
from fractions import gcd
def ekp(a,b):
  return(a*b/gcd(a,b))
```

Τέλος συνδυάζοντας τα προηγούμενα το συνολικό πρόγραμμα για να κάνουμε ομώνυμα τα κλάσματα $\frac{3}{5}$, $\frac{2}{3}$ και $\frac{5}{20}$ είναι:

```
from fractions import Fraction,gcd
def tiposemeparonomasti(k,p):
  """
  tiposemeparonomasti(k,p)
  Τύπωσε το κλάσμα k με παρονομαστή p
  """
  if p % k.denominator == 0:#αν το p είναι πολλαπλάσιο
                            #του τρέχοντος παρονομαστή (denominator)
                            #τότε μπορούμε να πολλαπλασιάσουμε
                            #όλο το κλάσμα με έναν συντελεστή
    synt = int(p // k.denominator)
    print(str(k.numerator * synt) + '/' + str(k.denominator * synt))
  else:#αν το p δεν είναι πολλαπλάσιο του τρέχοντος παρονομαστή
       #τότε τυπώνουμε το κλάσμα ως έχει
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
```

Μπορούμε να εισάγουμε δύο λειτουργίες από την ίδια βιβλιοθήκη χωρίζοντάς τες με κόμμα ",".
Θυμηθείτε ότι σε ένα κλάσμα a το a.denominator είναι ο παρονομαστής.

Το αποτέλεσμα του προγράμματος είναι:

```python
36/60
40/60
15/60
```

> Να εξετάσετε ποια από τα παρακάτω κλάσματα είναι ισοδύναμα:
(α)$\frac{2}{3},\frac{18}{27}$, (β)$\frac{3}{4},\frac{1}{2}, (γ)$\frac{7}{8},\frac{30}{40}$, (δ)$\frac{13}{14},\frac{26}{28}$.

```python
>>> print(Fraction(2,3)==Fraction(18,27))
True
>>> print(Fraction(3,4)==Fraction(1,2))
False
>>> print(Fraction(7,8)==Fraction(30,40))
False
>>> print(Fraction(13,14)==Fraction(26,28))
True
```
> Να μετατρέψεις καθένα από τα παρακάτω κλάσματα σε ισοδύναμο κλάσμα με παρονομαστή  τον αριθμό 100: 
(α)$\frac{3}{4}$ (β)$\frac{8}{5}$ (γ)$\frac{4}{20}$ (δ)$\frac{5}{2}$ (ε)$\frac{60}{75}$

Μπορούμε να χρησιμοποιήσουμε την συνάρτηση tiposemeparonomasti
```python
>>> tiposemeparonomasti(Fraction(3,4),100)
75/100
>>> tiposemeparonomasti(Fraction(8,5),100)
160/100
>>> tiposemeparonomasti(Fraction(4,20),100)
20/100
>>> tiposemeparonomasti(Fraction(5,2),100)
250/100
>>> tiposemeparonomasti(Fraction(60,75),100)
80/100
```

> Να μετατρέψεις τα παρακάτω κλάσματα σε ισοδύναμα με παρονομαστή τον αριθμό 3:

```python
>>> tiposemeparonomasti(Fraction(10,6),3)
5/3
>>> tiposemeparonomasti(Fraction(50,30),3)
5/3
>>> tiposemeparonomasti(Fraction(18,27),3)
2/3
```

> Να μετατρέψεις το κλάσμα $\frac{2}{3}$ σε ισοδύναμο κλάσμα με παρονομαστή:(α) 6, και (β) 15.

```python
>>> tiposemeparonomasti(Fraction(2,3),6)
4/6
>>> tiposemeparonomasti(Fraction(2,3),15)
10/15
```
> Να απλοποιήσεις τα κλάσματα: (α)$\frac{25}{30}$ (β) $\frac{12}{9}$ (γ) $\frac{32}{56}$

```python
>>> print(Fraction(25,30))
5/6
>>> print(Fraction(12,9))
4/3
>>> print(Fraction(32,56))
4/7
```
## Πρόσθεση και αφαίρεση κλασμάτων

> Το συνεργείο του Δήμου φύτεψε σε μια μέρα τα $\frac{4}{12}$ μιας πλατείας με λουλούδια. Την επόμενη ήμερα που ο καιρός δεν ήταν καλός φύτεψε μόνο τα $\frac{3}{12}$ της πλατείας. Ποιο τμήμα της πλατείας είχε φυτέψει, συνολικά, στο τέλος της δεύτερης ημέρας;

```python
>>> print(Fraction(4,12) + Fraction(3,12)(
7/12
```

> Ένα φορτηγό κάλυψε σε μία ώρα τα 2/5 της διαδρομής Πάτρα - Τρίπολη. Ποιο μέρος της διαδρομής του μένει να καλύψει ακόμη;

```python
>>> print(1-Fraction(2,5))
3/5
```

> Μια βρύση γεμίζει, σε 1 ώρα, τα $\frac{2}{5}$ της δεξαμενής. Μια άλλη βρύση γεμίζει το $\frac{1}{3}$ της ίδιας δεξαμενής, επίσης σε 1 ώρα. Αν και οι δύο βρύσες τρέχουν ταυτόχρονα μέσα στη δεξαμενή, τι μέρος της δεξαμενής θα γεμίσουν σε 1 ώρα;

```python
>>> print(Fraction(2,5)+Fraction(1,3))
11/15
```

> Να υπολογισθεί το άθροισμα 
> $$\frac{1}{4}+\frac{2}{4} + 3$$

```python
>>> print(Fraction(1,4)+Fraction(2,4) + 3)
15/4
```

> Να υπολογισθεί η διαφορά και το άθροισμα των κλασμάτων
$\frac{3}{12}$ και $\frac{7}{20}$.

```python
>>> print(Fraction(3,12) + Fraction(7,20))
3/5
>>> print(Fraction(7,20) - Fraction(3,12))
1/10
```
Για να τυπώσουμε ένα κλάσμα ως μεικτό θα εφαρμόσουμε τα εξής βήματα:
1. Βρίσκουμε το ακέραιο μέρος της διαίρεσης του αριθμητή με τον παρονομαστή έστω $\mu$.
2. Αν το $\mu$ είναι 0 τυπώνουμε το κλάσμα ως έχει (είναι μικρότερο της μονάδας), αλλιώς τυπώνουμε το $\mu$ και στη συνέχεια το κλάσμα που προκύπτει αν από το αρχικό κλάσμα αφαίρεσουμε το $\mu$.

```
def tiposemikto(k):
  m = k.numerator // k. denominator
  if m == 0:
  	print(k)
  else:
  	print(str(m) + " " + str(k-m))
```

Για παράδειγμα
```python
>>> tiposemikto(Fraction(15,4))
3 3/4
>>> tiposemikto(Fraction(5,2))
2 1/2
>>> tiposemikto(Fraction(38,12))
```
## Σύγκριση κλασμάτων
Η Μαρία είπε πως το ροζ χρώμα καταλαμβάνει τα $\frac{9}{48}$, το γαλάζιο τα $\frac{10}{48}$ και το πράσινο τα $\frac{7}{48}$. Ενώ ο Γιάννης είπε ότι το ροζ είναι τα $\frac{3}{16}$, το γαλάζιο τα $\frac{5}{24}$ και το πράσινο το $\frac{1}{8}$ του τετραγώνου.
Ποιος έχει δίκιο και ποιος όχι;

```python
>>> roz = Fraction(9,48)
>>> print(roz)
3/16
```
Άρα και η Μαρία και ο Γιάννης έχουν δίκο όσον αφορά το ροζ χρώμα.

```python
>>> galazio = Fraction(10,48)
>>> print(galazio)
5/24
```
Άρα και η Μαρία και ο Γιάννης έχουν δίκο όσον αφορά το γαλάζιο χρώμα.

Τέλος, όσον αφορά το πράσινο προκύπτει ότι:
```python
>>> prasino = Fraction(7,48)
>>> print(prasino)
7/48
>>> Fraction(7,48) == Fraction(1,8)
False
>>> Fraction(7,48) > Fraction(1,8)
True
```
Δηλαδή, το $\frac{7}{48}$ είναι μεγαλύτερο από το $\frac{1}{8}$.
~~Σχήμα~~

Παραδείγματα

> Να συγκριθούν τα κλάσματα $\frac{7}{10}$ και $\frac{7}{15}$

```python
>>> Fraction(7,10) > Fraction(7,15)
True
```

Άρα, $\frac{7}{10}>\frac{7}{15}$.

> Να συγκριθούν τα κλάσματα: $\frac{5}{8}$ και $\frac{4}{9}$.

```python
>>> Fraction(5,8) > Fraction(4,9)
True
```

Δεν χρειάζεται να τα μετατρέψουμε σε ομώνυμα, η python λύνει το πρόβλημα της σύγκρισης με τον δικό της τρόπο.

> Σύγκρινε τα κλάσματα (α) $\frac{3}{7}$ και $\frac{5}{7}$, (β) $\frac{3}{5}$ και $\frac{3}{9}$ και (γ) $\frac{4}{5}$ και $\frac{8}{12}$.

```python
>>> Fraction(3,7) < Fraction(5,7)
True
>>> Fraction(3,5) > Fraction(3,9)
True
>>> Fraction(4,5) > Fraction(8,12)
True
```

> Βάλε σε σειρά τα κλάσματα $\frac{3}{5},\frac{8}{15},\frac{5}{10},\frac{20}{15},\frac{7}{5}$

```python
>>> lista = [Fraction(31,10),Fraction(8,15),Fraction(5,10),Fraction(20,15),Fraction(7,5)]
>>> print(",".join([str(x) for x in sorted(lista)]))
1/2,8/15,4/3,7/5,31/10
```

# Πολλαπλασιασμός κλασμάτων
```python
#Pollaplasiasmos klasmatwn

x = Fraction(3,7)*Fraction(70,6)*Fraction(8,5)
print(x)

x = 3*Fraction(3,4)
print(x)

x = 7*Fraction(10,14)
print(x)

x = Fraction(4,2)*2
print(x)

x = Fraction(5,100)*10
print(x)

x = Fraction(2,5)*Fraction(7,8)
print(x)

x = Fraction(8,10)*Fraction(100,5)
print(x)

x = Fraction(4,9)*Fraction(5,9)
print(x)

x = Fraction(3,2)*Fraction(2,15)
print(x)

ori = [Fraction(5,7),Fraction(3,2),1,Fraction(3,4)]
kat = [Fraction(7,5),Fraction(2,3),1,Fraction(4,3)]
print("\n".join([",".join([str(k*o).rjust(5) 
  for o in ori]) for k in kat]))
  
x = (2+Fraction(1,3))*Fraction(3,21)
print(x)

x = (4+Fraction(1,5))*(2+Fraction(1,2))
print(x)

x = (3+Fraction(1,8))*10
print(x)

x = (1+Fraction(2,3))*Fraction(3,2)
print(x)

klasmata = [Fraction(4,7),Fraction(72),Fraction(5,8),Fraction(1,3),Fraction(739,8),Fraction(1)]
print(",".join([str(1/k) for k in klasmata]))

x = Fraction(6,5) + Fraction(3,5)*Fraction(1,4)
print(x)

x = (Fraction(6,5)+Fraction(3,5))*Fraction(1,4)
print(x)

x = (Fraction(6,5)-Fraction(3,5))*Fraction(1,4)
print(x)

x = (Fraction(7,3)+Fraction(2,15))*Fraction(3,8)
print(x)

x = (Fraction(7,3)-Fraction(2,15))*Fraction(3,8)
print(x)

x = Fraction(7,3)-Fraction(2,15)*Fraction(3,8)
print(x)
"""

x = Fraction(Fraction(2,3),Fraction(10,9))
print(x)

x = Fraction(4,Fraction(9,8))
print(x)

x = Fraction(Fraction(7,10),5)
print(x)

x = Fraction((Fraction(3,10)+Fraction(1,2)),(Fraction(4,3)-Fraction(4,6)))
print(x)

def rhind(x):
  """calculate (2/3)*(1/x)"""
  if not x%2 == 1:
    return(None)
  else:
    return(Fraction(1,2*x)+Fraction(1,6*x))
  
print(rhind(7) == Fraction(2,3)*Fraction(1,7))
```