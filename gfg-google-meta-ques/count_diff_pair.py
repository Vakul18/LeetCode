"""
Given an integer array of size n and a non-negative integer k, count all distinct pairs with a difference equal to k, i.e., A[ i ] - A[ j ] = k.
 
"""

#User function Template for python3
from collections import defaultdict
class Solution:
  def TotalPairs(self, nums, k):
    s = defaultdict(int)
    s1 = set()
    for num in nums:
      s[num] += 1
    
    for num in nums:
      if (num - k) in s and s[num - k] > (1 if k == 0 else 0):
        s1.add((num, num - k))

    return len(s1)
        