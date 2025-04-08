"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

arr : [1,2,0,-2,1,-4,2]

arr : [-4,-2,-3]

max_sum = arr[0], curr_sum = arr[0]

1. loop through array
  prev_sum = curr_sum
  curr_sum += element
  
  max_sum = max(max_sum, elem, curr_sum)

  if curr_sum < prev_sum:
    curr_sum = 0
 
[-1,1,2,1]

[-2,3,1,3]
 
"""
from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return None

    curr_sum, max_sum = 0, float('-inf')
    for idx in range(0,len(nums)):
      num = nums[idx]
      curr_sum += num

      max_sum = max(max_sum, curr_sum)

      if curr_sum < 0:
        curr_sum = 0
    

    return max_sum
    


