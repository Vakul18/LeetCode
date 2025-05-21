"""
Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.


Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6] 
         0  1  2  3  4  5  6  7  8 
arr[] = [0, 2, 3, 1, 4, 5, 2, 3, 6]
                  |
i = 3 , k = 3
q = [3, 2]
op = [3, 3]

invariant : at each iteration top value in queue signifies the max element of curr win which is i.e i - k - 1 -> i
"""
from collections import deque

class Solution:
  def maxOfSubarrays(self, arr, k):
    n = len(arr)
    if k > n:
      return []
    op = []
    q = deque()
    for i in range(n):
      while q and arr[i] >= arr[q[0]]:
        q.popleft()

      q.appendleft(i)

      if q[-1] <= i - k:
        q.pop()

      if i >= k-1:
        op.append(arr[q[-1]])
    return op