def romanToDec(romStr):
  romNum = {}
  romNum[1000] = 'M'
  romNum[900]  = 'CM'
  romNum[500]  = 'D'
  romNum[400]  = 'CD'
  romNum[100]  = 'C'
  romNum[90]   = 'XC'
  romNum[50]   = 'L'
  romNum[40]   = 'XL'
  romNum[10]   = 'X'
  romNum[9]    = 'IX'
  romNum[5]    = 'V'
  romNum[4]    = 'IV'
  romNum[1]    = 'I'
  
  result = 0
  
  v = list(sorted(romNum.keys(),reverse = True))
  value = v.pop(0)
  while romStr != '':
    chars = len(romNum[value])
    if (romStr[:chars] == romNum[value]):
      result += value
      romStr = romStr[chars:]
    else:
      if v == []:
        #there are symbols left that are
        #not parsed
        return(None)
      else:
        value = v.pop(0)
  return(result)

print(romanToDec('MCDXXIV'))
