"""
Given an array arr[], where each element is at most k away from its target position, you need to sort the array optimally.
Note: You need to change the given array arr[] in place.

Input: arr[] = [6, 5, 3, 2, 8, 10, 9], k = 3
Output: [2, 3, 5, 6, 8, 9, 10]
Explanation: The sorted array will be 2 3 5 6 8 9 10

[2, 3, 5, 6, 8, 9, 10], k = 3
                    |
hp = [6, 8, 9, 10]

"""
import heapq

class Solution:
  def nearlySorted(self, arr, k):
    n = len(arr)
    hp = []
    idx, idx_s = 0, 0
   
    while idx < n:
      heapq.heappush(hp, arr[idx])
   
      if len(hp) == k+1:
        num = heapq.heappop(hp)
        arr[idx_s] = num
        idx_s += 1
      idx += 1

    while hp:
      arr[idx_s] = heapq.heappop(hp)
      idx_s += 1

    return