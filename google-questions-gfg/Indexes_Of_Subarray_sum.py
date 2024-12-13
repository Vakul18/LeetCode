"""
Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray.


[2, 3, 5, 1], 5 -> [3,3]

[2, 3, 5, 1], -1 -> [3,4]

[19 23 15 6 6 2 28 2], 2
 r l

3 , 1, 4 0

currSum = 19


"""

#User function Template for python3
class Solution:
    def subArraySum(self, arr, target):
        if len(arr) == 0:
            return [-1]
        left = 0
        right = 0
        currSum = arr[left]
        while currSum != target and  left < len(arr) and right < len(arr):
            if currSum > target:
                currSum -= arr[left]
                left += 1
            if currSum < target:
                right += 1
                if right < len(arr):
                    currSum += arr[right]			
        
        if currSum == target:
            return [left+1, right+1]
        else:
            return [-1]

