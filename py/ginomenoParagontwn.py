class ginomenoparagontwn():
  def __init__(self,n):
    self.paragontes = []
    self.dinameis = {}
    if type(n) == int:
      self.arithmos = n
      while n > 1:
        for i in range(2,n+1):
          if n%i == 0:
            n = n // i
            self.paragontes.append(i)
            break
      self.paragontes = sorted(self.paragontes)
      for i in self.paragontes:
        if i not in self.dinameis:
          self.dinameis[i] = self.paragontes.count(i)
    elif type(n) == dict:
      self.arithmos = 1
      self.dinameis = n
      for i in n:
        self.arithmos *= i**n[i]
      for i in n:
        self.paragontes.extend([i]*n[i])
      self.paragontes = sorted(self.paragontes)
    if len(self.paragontes) > 1:
      self.einaiPrwtos = False
    else:
      self.einaiPrwtos = True
  
  def mkd(self,other):
    if type(other) == int:
      other = ginomenoparagontwn(other)
    dinameismkd = {}
    for i in self.dinameis:
      if i in other.dinameis:
        dinameismkd[i] = min(self.dinameis[i],other.dinameis[i])
    if dinameismkd == {}:
      return(ginomenoparagontwn({1:1}))
    else:
      return(ginomenoparagontwn(dinameismkd))
      
  def ekp(self,other):
    if type(other) == int:
      other = ginomenoparagontwn(other)
    dinameisekp = self.dinameis
    for i in other.dinameis:
      if i in dinameisekp:
        dinameisekp[i] = max(dinameisekp[i],other.dinameis[i])
      else:
        dinameisekp[i] = other.dinameis[i]
    return(ginomenoparagontwn(dinameisekp))
    
  def __repr__(self):
    return(str(self.arithmos) + ':' + '*'.join([str(x) + '^' + str(self.dinameis[x]) 
      for x in self.dinameis]) + ':' + '*'.join([str(x) for x in self.paragontes]) + 
      (',πρώτος' if self.einaiPrwtos else ""))

