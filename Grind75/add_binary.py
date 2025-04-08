"""
Given two binary strings a and b, return their sum as a binary string.

a, b = '11', '1' -> '100'

1. find min, max
2. add leading zeroes to min, to bring it on par with max
3. set carry = 0
3. loop throught each char from right to left.
     3.1 convert the chars to int
     3.2 sum them with 
     3.3 if sum == 2 then carry = 1, sum = 0
     3.4 if sum == 3 then carry = 1 , sum = 1
     3.5 else sum = s, carry = 0
        
"""
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    max_s, min_s = '', ''
    if len(a) > len(b):
      max_s = a
      min_s = b
    else:
      max_s = b
      min_s = a

    while len(min_s) < len(max_s):
      min_s = '0' + min_s
    res = ''
    carry = 0
    for idx in range(len(max_s) - 1, -1, -1):
      sum = carry + int(max_s[idx]) + int(min_s[idx])
      
      if sum == 2:
        carry = 1
        sum = 0
      elif sum == 3:
        carry = 1
        sum = 1
      else:
        carry = 0
      res = str(sum) + res
    if carry != 0:
      res = '1' + res
    return res
    
------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2) + int(b,2)
        return (bin(c)[2:])

