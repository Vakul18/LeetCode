"""
4 Sum - All Quadruples

Given an array arr[] of integers and another integer target. Find all unique quadruples from the given array that sums up to target.

Note: All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4.

Examples :

Input: arr[] = [0, 0, 2, 1, 1], target = 3
Output: [0, 0, 1, 2] 
Explanation: Sum of 0, 0, 1, 2 is equal to 3.
Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23
Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
Explanation: Sum of 2, 3, 8, 10 is 23, sum of 2, 4, 7, 10 is 23 and sum of 3, 5, 7, 8 is also 23.
Input: arr[] = [0, 0, 2, 1, 1], target = 2
Output: [0, 0, 1, 1] 
Explanation: Sum of 0, 0, 1, 1 is equal to 2.
"""
class Solution:
  def fourSum(self, arr, target):
    n = len(arr) 
    result = []
    arr_s = sorted(arr)

    for i in range(n-3):
      if i > 0 and arr_s[i] == arr_s[i-1]:
        continue
      for j in range(i+1, n-2):
        if j > i+1 and arr_s[j] == arr_s[j-1]:
          continue
        l, r = j + 1, n-1
        while l < r:
          s = arr_s[i] + arr_s[j] + arr_s[l] + arr_s[r]
          if s == target:
            result.append([arr_s[i], arr_s[j], arr_s[l], arr_s[r]])
            while l < r and arr_s[l] == arr_s[l+1]:
              l += 1
            while l < r and arr_s[r] == arr_s[r-1]:
              r -= 1
            l += 1
            r -= 1
          elif s < target:
            l += 1
          else:
            r -= 1

    return result