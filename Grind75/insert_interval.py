"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

[1,2] [3,5] [10,11] [12,13] | [6,7]; [4,24]; [6,24]; [4,7]





"""
from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
    updated_intervals = []
    is_inserted = False
    for interval in intervals:
      if not is_inserted:
        if newInterval[1] < interval[0]:  # if it can be inserted before
          updated_intervals.extend([newInterval, interval[:]])
          is_inserted = True
        elif newInterval[0] <= interval[1]:  # overlap found
          updated_intervals.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[1])])
          is_inserted = True
        else:
          updated_intervals.append(interval[:])

      else:
        if interval[0] <= updated_intervals[-1][1]:  #overlap
          updated_intervals[-1][0] = min(interval[0], updated_intervals[-1][0])
          updated_intervals[-1][1] = max(interval[1], updated_intervals[-1][1])
        else:
          updated_intervals.append(interval)

    if not is_inserted:
      updated_intervals.append(newInterval)
    return updated_intervals
        
-----------------------------------------------------------------------------------------------

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i::]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0],newInterval[0]), max(interval[1], newInterval[1])]

        res.append(newInterval)
        return res




    
        