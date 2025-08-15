"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

[-1,0,1,2,-1,-4]

[-4,-1,-1,-1,0,1,2,2]

- sort the array
- iterate over the array, find two elements such that sum is - curr num
- skip duplicates
- repeat

"""


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums_s = sorted(nums)
    n = len(nums_s)
    prev_num = float('inf')
    result = []
    for idx, num in enumerate(nums_s):
      if num == prev_num:
        continue

      target = -num
      l, r = idx + 1, n-1

      while l < r:
        curr_sum = nums_s[l] + nums_s[r]
        if curr_sum == target:
          result.append([nums_s[idx], nums_s[l], nums_s[r]])
          r = r - 1
          l = l + 1
          while nums_s[r] == nums_s[r+1] and l < r:
            r = r - 1
          while nums_s[l] == nums_s[l-1] and l < r:
            l = l + 1 
        elif curr_sum > target:
          r = r - 1
        else:
          l = l + 1

      prev_num = num

    return result
        
      