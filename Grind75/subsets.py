"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

n = len(nums)
2^n

n = 3
8 -> 000, 001,
"""
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)

    total_subsets = 2**n
    res = []
    for i in range(total_subsets):
      set = []
      for idx, elem in enumerate(nums):
        if (1 << idx) & i:
          set.append(elem)
      res.append(set)
    return res

--------------------

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bk(i, path):
            res.append(path)
            
            for j in range(i, len(nums)):
                bk(j + 1, path + [nums[j]])
                
        bk(0, [])
        return res


                
        
        

