"""
Given an array arr[] of sorted and distinct positive integers. The task is to find the length of the longest arithmetic progression in a given array.

Note: A sequence seq is an arithmetic progression if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
                 -6 -3  -3  -1  -5
Input:arr[] = [1, 7, 10, 13, 14, 19]
Output: 4

19 : [5:5, 6:4, 9:3, 12:2, 18:1]
14 : [1, 4, 7, 13]
13 : [3, 6, 12]
7 : [6]
1 : []

"""
#User function Template for python3

class Solution:
  def lengthOfLongestAP(self,arr):
    n = len(arr)

    if n <= 2:
      return n

    diff_dict = {}

    max_ap_len = 0
    for i in range(n-1  , -1, -1):
      for j in range(i+1, n):
        diff = arr[i] - arr[j]
        if (j, diff) in diff_dict:
          diff_dict[(i, diff)] = diff_dict[(j, diff)] + 1
        else:
         diff_dict[(i, diff)] = 2
        max_ap_len = max(max_ap_len, diff_dict[(i, diff)])
    
    return max_ap_len

