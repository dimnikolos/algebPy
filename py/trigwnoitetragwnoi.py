import math
def trigwnos(n):
  return(int(n*(n+1)/2))

def triwnoitetragwnoi():
  n = 1
  while True:
    if math.floor(math.sqrt(trigwnos(n))) == math.sqrt(trigwnos(n)):
      print(trigwnos(n))
    n += 1

triwnoitetragwnoi()
