from fractions import Fraction

ori = [Fraction(5,7),Fraction(3,2),1,Fraction(3,4)]
kat = [Fraction(7,5),Fraction(2,3),1,Fraction(4,3)]
print(" "*5+", ",end=" ")
for orizontio in ori:
    print(str(orizontio).rjust(5),end=", ")
print()
print("-"*35)
for katheto in kat:
    print(str(katheto).rjust(5),end=", |")
    for orizontio in ori:
        print(str(orizontio*katheto).rjust(5),end=", ")
    print()
