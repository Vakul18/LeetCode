"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


################
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set()
    for num in nums:
      num_set.add(num)
    max_len = 0
    for num in num_set:
      if (num - 1) in num_set:
        continue
      curr_len = 1
      curr_num = num
      while curr_num + 1 in num_set:
        curr_len += 1
        curr_num += 1
      max_len = max(max_len, curr_len)

    return max_len
          
############slower approach##############
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    num_map = dict()
    for num in nums:
      if num not in num_map:
        num_map[num] = 1
    
    visited = set()
    max_len = 1
    for num in nums:    
      if num in visited:
        continue
      
      visited.add(num)
      curr_len = num_map[num]
      curr_num = num + 1
      while curr_num in num_map and (curr_num not in visited):
        curr_len += 1
        curr_num += 1

      if curr_num in visited:
        curr_len += num_map[curr_num]

      max_len = max(curr_len, max_len)
      num_map[num] = curr_len

    return max_len