"""
Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. It is guaranteed that the size of array is at-least k.

Example 1:

Input : 
n = 4
a[] = {1, -2, 2, -3}
k = 2
Output : 
1
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, -2, 2}
Example 2:
Input :
n = 6 
a[] = {1, 1, 1, 1, 1, 1}
k = 2
Output : 
6
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, 1, 1, 1, 1, 1}

a[] = {1, -2, 2, -3}

1,-2 1,-2,2  1,-2,2,-3

-2,2 -2,2,-3

k = 2
1, -2, 2, -3, 10, 14, 17, -20

-10, -1 , -2


"""
#User function Template for python3

class Solution():
  def maxSumWithK(self, a, n, k):
    if k > n or k <= 0:
      raise ValueError("Invalid k")
    
    max_sum_ending_at = [0] * n
    max_sum_ending_at[0] = a[0]
    for i in range(1, n):
      max_sum_ending_at[i] = max(a[i], max_sum_ending_at[i-1] + a[i])
    
    win_sum = sum(a[:k])
    max_sum = win_sum
    for i in range(k, n):
      win_sum = win_sum + a[i] - a[i-k]

      max_sum = max(max_sum, win_sum, max_sum_ending_at[i-k] + win_sum) 

    return max_sum




 
        
        
        
      





