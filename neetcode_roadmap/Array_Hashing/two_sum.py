"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    idx_val_map = dict()

    for idx, num in enumerate(nums):
      if num not in idx_val_map:
        idx_val_map[num] = set([idx])
      else:
        idx_val_map[num].add(idx)


    for idx, num in enumerate(nums):
      leftover = target - num

      if leftover in idx_val_map and ((idx not in idx_val_map[leftover]) or (idx in idx_val_map[leftover] and len(idx_val_map[leftover]) > 1)):
        left_over_idx = -1
        for target_idx in idx_val_map[leftover]:
          if target_idx != idx:
            left_over_idx = target_idx
            break

        return [idx, left_over_idx]

    return None
###################

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    idx_val_map = dict()

    for idx, num in enumerate(nums):
      complement = target - num
      if complement in idx_val_map:
        return [idx, idx_val_map[complement]]

      idx_val_map[num] = idx

    return []

        