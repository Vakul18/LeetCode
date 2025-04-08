"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""
class Solution:
  def sortColors(self, nums: List[int]) -> None:
    low, mid = 0,0
    high = len(nums) - 1

    while mid <= high:
      if nums[mid] == 0:
        nums[mid], nums[low] = nums[low], nums[mid]
        mid += 1
        low += 1
      elif nums[mid] == 1:
        mid+=1
      else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

    return
        