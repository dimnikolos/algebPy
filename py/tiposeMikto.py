from fractions import Fraction

def tiposeMikto(k):
  m = k.numerator // k. denominator
  if m == 0:
    print(k)
  else:
    print(str(m) + " " + str(k-m))
