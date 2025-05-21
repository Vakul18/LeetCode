"""
https://www.geeksforgeeks.org/problems/maximum-index3307/1?page=1&company=Google,Facebook&difficulty=Medium&sortBy=difficulty

Given an array, arr[] of non-negative integers. The task is to return the maximum of j - i (i<=j) subjected to the constraint of arr[i] <= arr[j].


Input: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6


Input: arr[] = [18, 17]
Output: 0

Input: arr[] = [10, 10, 10, 10]
Output: 3

"""

#User function Template for python3
class Solution:
	def maxIndexDiff(self,arr):
	    n = len(arr)
		rMax = [arr[idx] for idx in range(n)]
		curr_max = arr[n-1]
		for idx in range(n-1, -1, -1):
		    rMax[idx] = max(rMax[idx], curr_max)
		    curr_max = rMax[idx]
		
		i, j, max_diff = 0, 0, 0
		while i < n and j < n:
		    if rMax[j] >= arr[i]:
		        max_diff = max(max_diff, j - i)
		        j += 1
		    else:
		        i += 1
		
        return max_diff

###############################################

#User function Template for python3
class Solution:
	def maxIndexDiff(self,arr):
	    n = len(arr)
		rMax = [arr[idx] for idx in range(n)]
		curr_max = arr[n-1]
		for idx in range(n-1, -1, -1):
		    rMax[idx] = max(rMax[idx], curr_max)
		    curr_max = rMax[idx]
		
		i, j, max_diff = 0, 0, 0
		while i < n and j < n:
		    if rMax[j] >= arr[i]:
		        max_diff = j - i
		    else:
		        i += 1
            j += 1
		
        return max_diff