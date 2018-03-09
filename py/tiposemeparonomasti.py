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
