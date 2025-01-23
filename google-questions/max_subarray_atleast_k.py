"""
Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. It is guaranteed that the size of array is at-least k.

[2,3,7], 1 -> 17

[2,-1,2,-10,22, -100, 15, 15], 2 -> 15
            [  2,  -1,   2, -10,  22,-100, 15, 15]
left_sum =  [  2,   1,   3,  -7,  15, -85,-70,-55]
right_sum = [-35, -37, -36, -38, -48, -70, 30, 15]


[2,-1,2,-10,22], 2 -> 15




"""

class Solution():
    def maxSumWithK(self, arr, n, k):
        

        pref_sum = []
        pref = 0
        for element in arr:
            pref += element
            pref_sum.append(pref)
        
        curr_max = pref_sum[k-1]
        max_sum = pref_sum[k-1]
        """
        arr = [2,-1,2,-10,22], k = 1
        pref_sum = [2,1,3,-7,15]
        idx = 5
        curr_max = 22
        curr_max = max(3 - 10, -10) = -7
        max_sum = 3
        """
        for idx in range(k,n):
            curr_max = max(curr_max + arr[idx], pref_sum[idx] - pref_sum[idx - k])
            max_sum = max(curr_max, max_sum)
  
        return max_sum
