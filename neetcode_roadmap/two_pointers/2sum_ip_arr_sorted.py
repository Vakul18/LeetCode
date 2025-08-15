"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    l, r = 0, n-1

    while l < r:
      curr_sum = numbers[l] + numbers[r]
      if curr_sum == target:
        return [l + 1, r + 1]
      elif curr_sum < target:
        l += 1
        while l < r and numbers[l] == numbers[l-1]:
          l += 1
      elif curr_sum > target:
        r -= 1
        while l < r and numbers[r] == numbers[r+1]:
          r -= 1
       
      
    return []
        