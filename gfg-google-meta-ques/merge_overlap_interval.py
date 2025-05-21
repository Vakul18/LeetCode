"""
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.
"""
class Solution:
  def mergeOverlap(self, arr):
    n = len(arr)
    if n < 2:
      return arr
 
    arr_s = sorted(arr, key= lambda x : x[0])
    idx = 1
    merged_intervals = [arr_s[0]]

    while idx < n:
      if arr_s[idx][0] <= merged_intervals[-1][1]:
        merged_intervals[-1][1] = max(arr_s[idx][1], merged_intervals[-1][1])
      else:
        merged_intervals.append(arr_s[idx])
      idx += 1

    return merged_intervals
    