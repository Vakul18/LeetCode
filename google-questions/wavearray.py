"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.\

[1,2,3,4,5,6] -> [2,1,4,3,6,5]


[1,2,3,4,5] -> [2,1,4,3,5]

"""

from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        n = len(arr)
        idx = 0
        while (idx+1) < n:
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            idx += 2

