"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

|   |  
|   |   
| | | |
"""
class Solution:
  def maxArea(self, arr: List[int]) -> int:
    n = len(arr)
    l, r = 0, n-1
    max_vol = 0
    while l < r:
      curr_vol = min(arr[l], arr[r]) * (r-l)
      max_vol = max(curr_vol, max_vol)
      
      if arr[l] < arr[r]:
        l = l + 1
      elif arr[r] < arr[l]:
        r = r - 1
      else:
        r = r - 1
        l = l + 1
    return max_vol
    