"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.

[-1,4,8,5,-19,-1000]

"""
class Solution:
    def maxSubArraySum(self,arr):
        curr_sum = 0
        max_sum = float('-inf')

        for idx in range(0,len(arr)):
            curr_sum += arr[idx]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
