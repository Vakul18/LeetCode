"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

[1,2,3] -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

 1 2 3
 1 3 2

 2 1 3
 2 3 2

 3 1 2
 3 2 1

 1
   1
     1

[1,2,3,4] -> [[1,2,3,4], [1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2]]


1,2,3
0 1 2
             -
     /       |       \
    0        1        2 
   / \       /\       /\
  1   2     0  2     1  0
 /     \   /    \   /    \
2       1 2      0  0     1


[1,2,3]

create_permute(nums[n], n, chosen[n], permutation)
 if n == 0:
  return permutation
 all_permutations = []
 loop through chosen not set as False
  set chosen as true
  curr_permutation = permutation[:] + curr_chosen
  created_permutations = create_permute(nums, n-1, chosen, curr_permutation)
  all_permutations.append(created_permutations)
  set chose as False

 return all_permutations

return create_permute(nums, n, choset, [])

[1,2,3]

chose : T,T,T
"""
from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    all_perm = []
    self.create_permute(nums, len(nums), [True for _ in range(len(nums))], [], all_perm)
    return all_perm

  def create_permute(self, nums: List[int], n : int, chosen : List[bool], permutations : List[int], all_perm : List[List[int]]):
    if n == 0:
      all_perm.append(permutations)
      return

    for idx in range(len(nums)):
      if not chosen[idx]:
        continue

      chosen[idx] = False
      curr_permutation = permutations[:] + [nums[idx]]
      created_permutation = self.create_permute(nums, n-1, chosen, curr_permutation, all_perm)
      chosen[idx] = True






---------------------------

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                result.append(nums[:])

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return result


        



  
    



















    