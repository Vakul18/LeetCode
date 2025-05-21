"""
Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order. 

Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]

"""
import heapq

class Solution:
  def kLargest(self, arr, k):
    if k <=0:
      return []

    hp = []

    for num in arr:
      if len(hp) < k:      	
        heapq.heappush(hp, num)
      elif num > hp[0]:
        heapq.heapreplace(hp, num)

    return sorted(hp, reverse = True)


------------------------
import random

class Solution:
  def kLargest(self, arr, k):
    def quickselect(s, e):
      pivot = random.randint(s, e)
      arr[e], arr[pivot] = arr[pivot], arr[e]
      
      pivot= s-1

      for idx in range(s, e):
        if arr[idx] >= arr[e]:
          pivot += 1
          arr[pivot], arr[idx] = arr[idx], arr[pivot]
      pivot += 1
      arr[e], arr[pivot] = arr[pivot], arr[e]
      return pivot
    l, r = 0 , len(arr)-1
    k_arr = []
    while l <= r:
      m = quickselect(l, r)

      if m == k-1:
        k_arr= arr[:k]
        break

      if m > k-1:
        r = m - 1
      else:
        l = m + 1

    return sorted(k_arr, reverse = True) 