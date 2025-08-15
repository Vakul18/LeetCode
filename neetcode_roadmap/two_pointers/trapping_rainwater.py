"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
  def trap(self, height: List[int]) -> int:
    n = len(height)
    left_max, right_max = 0, 0
    l, r = 0, n-1
    trapped_water = 0
    while l < r:
      if height[l] < height[r]:
        if height[l] > left_max:
          left_max = height[l]
        else:
          trapped_water += left_max - height[l]
        l += 1
      else:
        if height[r] > right_max:
          right_max = height[r]
        else:
          trapped_water += right_max - height[r]
        r = r - 1
    return trapped_water