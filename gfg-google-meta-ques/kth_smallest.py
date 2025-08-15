"""
Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

[4, 1, 9, 0], 2 -> 1

"""
import random
class Solution:
  def kthSmallest(self, arr,k):
    l, r = 0, len(arr)-1
    def quickSelect(s, e):
      r_idx = random.randint(s,e)
      arr[r_idx], arr[e] = arr[e], arr[r_idx]
      
      pivot, i = s-1, s
      
      while i < e:
        if arr[i] < arr[e]:
          pivot += 1
          arr[pivot], arr[i] = arr[i], arr[pivot]
        i += 1
      pivot += 1
      arr[pivot], arr[e] = arr[e], arr[pivot]
      return pivot
      
    while l <= r:
      m = quickSelect(l, r)
      if m == k-1:
        return arr[k-1]

      if m < k-1:
        l = m+1
      else:
        r = m - 1

    return -1