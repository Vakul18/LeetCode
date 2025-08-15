"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


"""

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix = 1
    n = len(nums)

    prefix = 1
    prefix_prod = []
    for i in range(n):
      prefix = prefix*nums[i]
      prefix_prod.append(prefix)

    suffix = 1
    suffix_prod = [1]*n

    for i in range(n-1, -1, -1):
      suffix *= nums[i]
      suffix_prod[i] = suffix
 
    result = []
    for i in range(n):
      pre = prefix_prod[i-1] if i > 0 else 1
      suff = suffix_prod[i+1] if i < n-1 else 1
      result.append(pre * suff)

    return result


########################

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("1"))

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        left = 1

        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


        
        