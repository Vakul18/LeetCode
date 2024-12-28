"""
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

[2,3,1,3,0], 2 -> 1

bubble sort k times -> O(nk)

quick sort partition method -> O(klogn)


[2,3,1,3,0], 2
[0,1,2,3,3]
left = 0, right = 4
partition(0,4)
  pivotIdx = 2
  idx = 2, pivotIdx = 1
  
  


"""
import random 

class Solution:
    def swap(self, arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    def partition(self, left, right, arr):
        pivotIdx = random.randint(left,right)
        self.swap(arr, right, pivotIdx)
        idx = left
        pivotIdx = left
        
        while(idx < right):
            if arr[idx] < arr[right]:
                self.swap(arr, idx, pivotIdx)
                pivotIdx += 1
            idx += 1

        self.swap(arr, right, pivotIdx)

        return pivotIdx                 
                
    def kthSmallest(self, arr,k):
        left = 0
        right = len(arr) - 1
        k -= 1
        while left <= right:
            idx = self.partition(left, right, arr)
            if idx == k:
                return arr[idx]

            if idx < k:
                left = idx + 1
            else:
                right = idx - 1
            
