"""
Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.

[4, 2, 6, 1, 1], 3 -> 1

k = 3
curr_max = 2
idx = 0

33 38 46 24 26 6 42 28
2 -> [38, 46, 46]

(-46,2)(-33, 0)(-24,3)

idx = 3


"""
import heapq

class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        if n < k:
            return None

        priorityQueue = [(-arr[idx], idx) for idx in range(0,k)]
        
        heapq.heapify(priorityQueue)
        
        result = [-priorityQueue[0][0]]

        for idx in range(k, n):
            while len(priorityQueue) > 0 and priorityQueue[0][1] <= idx-k:
                heapq.heappop(priorityQueue)
                
            heapq.heappush(priorityQueue, (-arr[idx], idx))
            result.append(-priorityQueue[0][0])

        return result
            

            

