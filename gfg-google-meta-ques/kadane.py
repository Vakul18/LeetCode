"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.
"""
class Solution:
    def maxSubArraySum(self, arr):
        if len(arr) == 0:
            return -1
        elif len(arr) == 1:
            return arr[0]
        max_sum = arr[0]
        curr_sum = 0
        for idx in range(0, len(arr)):
            num = arr[idx]
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum <0:
                curr_sum = 0
        return max_sum