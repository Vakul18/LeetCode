"""
power using simple arithmetic(+, -, *, /)

a = 3, b = 10

 = 3^50 * 3^50 = 3^25*3^25 = 3^17*3*3^17*3 = 3^8*3 = 3^4 = 3^2 = 3



dp[0-b]
dp[0] = 1
dp[1] = 3*dp[1-1]
dp[2] = 3*dp[2-] 
"""
import math
def power(a, b):
  if b == 0:
    return 1
  
  return power(a, b//2)*power(a, b//2) * (a if (b&1==1) else 1)

def power(a,b):
  if b == 0:
    return 1
  elif b == 1:
    return a
  n = abs(b)
  ans = a
  p = 2
  while p <= n:
    ans *= ans
    p *=2

  if n&1 == 1:
    ans *= a
  return ans if b >=0 else 1/ans
  
print(power(3,-8))
  
  
  
  

  
  
  