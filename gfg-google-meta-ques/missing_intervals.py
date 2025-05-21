"""
Given a sorted array arr[] of integers varying from range l to r. Find all the missing intervals range in array arr[] from the given range and return in sorted order.
Note: If no Integer is missing return {-1,-1}.

Input: arr[] = [1, 5, 6, 7, 9], l = 1, r = 9
Output: [{2, 4}, {8, 8}]



"""
class Solution:
  def missingIntervals(self, arr, l, r):

    missing_ranges = []
    n = len(arr)
    curr = l
    idx = 0
     
    while idx < n and curr > arr[idx]:
      idx += 1
    
    while idx < n and curr <= r:
      if arr[idx] != curr:
        next_curr = min(arr[idx]-1, r)
        missing_ranges.append([curr, next_curr])
        curr = arr[idx]
      
      idx += 1
      while idx < n and arr[idx] == arr[idx-1]:
        idx += 1 
      curr += 1

    if curr <= r:
      missing_ranges.append([curr, r])
   
    return missing_ranges if missing_ranges else [[-1,-1]]