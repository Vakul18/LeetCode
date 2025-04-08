"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""
class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
      return []

    sorted_intervals = sorted(intervals, key = lambda x : x[0])
    merged_intervals = [sorted_intervals[0]] 
    for idx in range(1, len(sorted_intervals)):
      last_interval = merged_intervals[-1]
      curr_interval = sorted_intervals[idx]

      if last_interval[1] < curr_interval[0]:
        merged_intervals.append(curr_interval)
      else:
        end_point = max(curr_interval[1], last_interval[1])
        last_interval[1] = end_point

    return merged_intervals 


-----------------------------------------------------------------------------------	


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # If merged list is empty or there is no overlap with the last interval, add it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

        
      