"""
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

[1, 2, 4, 1, 1, 1]

1 3 5 8 9 2 6 7 6 8 9
                  
"""

class Solution:
  def minJumps(self, arr):
    max_reach, last_end = 0, 0
    idx, n = 0, len(arr)
    jumps = 0
    while idx < n-1:
      max_reach  = max(max_reach, arr[idx] + idx)
      if idx == last_end:
        jumps += 1
        if max_reach == last_end:
          return -1
        last_end = max_reach
      idx += 1
    return jumps if max_reach >= n-1 else -1
    