"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

-2 6 -3 -10 0 2

max = -2
min = -2
i = 1
"""

#User function Template for python3
class Solution:
  def maxProduct(self,arr):
    min_prod, max_prod = arr[0], arr[0]
    max_val = max_prod
    for i in range(1, len(arr)):
      if arr[i] == 0:
        max_prod, min_prod = 1, 1
        max_val = max(max_val, 0)
        continue
      temp = max(max_prod * arr[i], min_prod * arr[i], arr[i])
      min_prod = min(max_prod * arr[i], min_prod * arr[i], arr[i])
      max_prod = temp
      max_val = max(max_val, max_prod)

    return max_val


######################################

#User function Template for python3
class Solution:
  def maxProduct(self,arr):
    pre, suff, n = 1, 1, len(arr)
    max_val = float('-inf')
    for i in range(len(arr)):

      if pre == 0:
        pre = 1
      if suff == 0:
        suff = 1
      
      pre *= arr[i]
      suff *= arr[n-i-1]
      max_val = max(max_val, pre, suff)
    

    return max_val


