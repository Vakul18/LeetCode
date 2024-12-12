"""
Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x. Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.

Note:  Return -1 if you can't reach the end of the array.

[2,0] -> 1
[2,3,1,0,0] -> 2


arr[i] + j >= (n-1)

shortpaths = [float('inf') for i in range(0,n)]
shortPaths = [,0]
idx
	for j in range(1, arr[idx])
	min(minPath, shortPaths[idx + j])

return shortPaths[0]


[2,0] 




[2,0,0,2,0]
idx = 0
max = 2
jumps = 0

idx =1
jumps = 1
max = 1
idx + arr[idx] >= n-1

idx=2
jumps = 2
max = 0
idx + arr[idx] >= n-1

"""
import math 

class Solution:
	def minJumps(self, arr):
		n = len(arr)
		shortestJumps = [float('inf') for _ in range(0,n)]
		
		#already at last pos
		shortestJumps[n-1] = 0
		
		"""
		n = 2
		shortestJumps = [1, 0]
		idx = 0
		minJumps = inf
		maxSpan = min(2,1) = 1
		minJumps = min(1, inf) = 1
		"""
		#loop from back to front 
		for idx in range(n-2, -1, -1):
			minJumps = float('inf')
			maxSpan = min(arr[idx], n-idx-1)
			
			# loop for all possible idexes reachable from curr idx
			for spanIdx in range(1, maxSpan+1):
				minJumps = min(shortestJumps[idx + spanIdx] + 1, minJumps)
			
			shortestJumps[idx] = minJumps

		if math.isinf(shortestJumps[0]):
			return -1
		else:
			return shortestJumps[0]
#######################################################################
"""
1 4 3 2 6 7
n = 6
jumps = 1
max_reach = 0
idx=1
max_reach = max(0, 4) = 8



"""
class Solution:
	def minJumps(self, arr):
		n = len(arr)
		
		if n<=1:
			return 0
		
		max_reach, jumps, idx, curr_win_end = 0, 0, 0, 0
		
		while (idx < n) and max_reach >= idx:

			max_reach = max(max_reach, idx + arr[idx])
			

			
			if idx == curr_win_end:
				jumps += 1
				
				if (max_reach) >= n-1:
					return jumps

				curr_win_end = max_reach
			
			idx += 1

		return (jumps) if (max_reach) >= n-1 else -1

		










			