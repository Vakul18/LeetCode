"""
Given an array arr[] and an integer target, the task is to find the sum of three integers in arr[] such that the sum is closest to target. 

Note: If multiple sums are closest to target, return the maximum one.

1 10 4 5
10

abs = 2,
clos = 8
1 4 5 10
    |  |
num = 2
curr_sum = 15


"""
class Solution:
  def closest3Sum(self, arr, target):
    n = len(arr)
    sort_arr = sorted(arr)
    abs_closest_sum, closest_sum = float('inf'), float('inf') 
    for i in range(n-2):
      num = sort_arr[i]
      l, r = i + 1, n-1
     
      while l < r:
        curr_sum = sort_arr[l] + sort_arr[r]
        if curr_sum + num == target:
          return target
        
        if abs(curr_sum + num - target) < abs_closest_sum:
          abs_closest_sum = abs(curr_sum + num - target)
          closest_sum = curr_sum + num 
        elif abs(curr_sum + num - target) == abs_closest_sum:
          closest_sum = max(curr_sum + num, closest_sum)
        
        if curr_sum + num > target:
          r -= 1
        else:
          l += 1
 
    return closest_sum 
------------------------------------

"""
1 2 2 4
4

abs = 2,
clos = 5

curr_sum = inf
l = 0, r = 1
m = 1
curr_sum = 5
"""

class Solution:
  def closest3Sum(self, arr, target):
    n = len(arr)
    sort_arr = sorted(arr)
    abs_closest_sum, closest_sum = float('inf'), float('inf') 
   
    l, r = 0, n-1

    while l < r:
      m = (l + r)//2
      curr_sum = sort_arr[l] + sort_arr[m] + sort_arr[r]

      if curr_sum == target:
        return target
     
      if abs(curr_sum - target) < abs_closest_sum:
        abs_closest_sum = abs(curr_sum - target)
        closest_sum = curr_sum
      elif abs(curr_sum - target) == abs_closest_sum:
        closest_sum = max(curr_sum, closest_sum)

      if curr_sum > target:
        r -= 1
      else:
        l += 1
 
  
    
 
    return closest_sum   

      