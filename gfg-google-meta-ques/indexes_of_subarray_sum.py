"""
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]

arr[] = [1, 5, 24, 27, 2]
               ||
            


"""
#User function Template for python3
class Solution:
  def subarraySum(self, arr, target):
    l,r = 0,0
    n = len(arr)
    curr_sum = arr[r]

    while r < n:
      if curr_sum == target:
        return [l+1, r+1]

      if curr_sum > target:
        if l == r:
          r += 1
          if r < n:
            curr_sum += arr[r]
        curr_sum -= arr[l]
        l += 1
      else:
        r += 1
        if r < n:
          curr_sum += arr[r]
          

    return [-1]
----------

def find_subarray_sum(arr, target):
    n = len(arr)
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > target:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return [start + 1, end + 1]

    return [-1]
         
    

