def xronosseld(wres,lepta,deutera):
    xronossedeutera = wres * 60 * 60 + lepta * 60 + deutera
    xronosselepta = xronossedeutera / 60
    print(xronosselepta,' min=',xronossedeutera,' s')

while True:
    wres = int(input('Ώρες:'))
    lepta = int(input('Λεπτα:'))
    deutera = int(input('Δευτερόλεπτα:'))
    xronosseld(wres,lepta,deutera)
