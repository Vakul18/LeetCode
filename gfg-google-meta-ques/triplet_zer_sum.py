"""
Find triplets with zero sum

Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false.
"""
#User function Template for python3

class Solution:
    # Function to find triplets with zero sum.
  def findTriplets(self, arr):
    arr = sorted(arr)
    n = len(arr)
    for i in range(2, n):
      l, r = 0, i-1
      num = arr[i]

      while l < r:
        s = arr[l] + arr[r]

        if s + num == 0:
          return True
        else:
          if s > -num:
            r -= 1
          else:
            l += 1

    return False
    