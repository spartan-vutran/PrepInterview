from typing import List, Tuple


def getSum(a: int, b: int) -> int:
  minValue, maxValue = (a,b) if a<b else (b,a)
  order = 0
  result = 0
  odd = False
  while maxValue > 0:
      fmin, fmax = minValue%2 if minValue>0 else 0, maxValue%2 
      minValue, maxValue = int(minValue/2), int(maxValue/2)
      if not odd:
          bsum = fmin^fmax
          if fmin == fmax and fmin == 1:
            odd = True
      else:
          bsum = fmin^fmax^1
          count = 0
          for i in (fmin, fmax, 1 if odd else 0):
             if i == 1:
                count +=1
          if count>=2:
            odd = True
          else:
            odd = False
      
      result += bsum*(2**order)
      order += 1
  return result + 1*(2**order) if odd == True else result

x=  [-2,0,-1]
print(getSum(10,8))