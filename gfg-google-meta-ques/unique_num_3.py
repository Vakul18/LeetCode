"""
Unique Number III

Given an array of integers arr[] where, every element appears thrice except for one which occurs once.
Find that element which occurs once.

arr = [2, 6, 6, 6]

2 : 010
6 : 110
"""
#User function Template for python3

class Solution:
  def getSingle(self, arr):
    result = 0
    for bit in range(32):
      mask = 1<<bit
      bit_count = 0
      for num in arr:
        bit_count += mask & num

      if bit_count % 3 != 0:
        result |= mask

    if result >= (1<<31):
      result -= (1<<32)

    return result

####################

class Solution:
  def getSingle(self, arr):
    result = 0
    for bit in range(32):
      mask = 1<<bit
      bit_count = 0
      for num in arr:
        bit_count += mask & num

      if bit_count % 3 != 0:
        if bit == 31:
          result -= mask
        else:
          result |= mask

    return result

########################

class Solution:
  def getSingle(self, arr):  
    ones, twos = 0, 0
    for num in arr:
      twos |= ones & num
      ones ^= num
      threes = ones & twos

      ones &= ~threes
      twos &= ~threes

    return ones
      


