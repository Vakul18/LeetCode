"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
"""
from collections import defaultdict
import heapq

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_map = defaultdict(int)
    result = []
    for num in nums:
      freq_map[num] += 1

    heap = []
    for key, value in freq_map.items():
      heapq.heappush(heap, (-value, key))


    for _ in range(k):
      result.append(heap[0][1])
      heapq.heappop(heap)

    return result      
      
    
        