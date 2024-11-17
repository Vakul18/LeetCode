"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

[1,2,3,4,5] = 20
[1,2,3,4] = 12
[1,2,3] = 6
[1,2] = 2

  
3-4
[1,2,3,4,5] = 24 
[1,2,4,5] = 40
[1,2,5] = 10
[1,5] =  

burstStates = [t, t, t, t, t]
6 + 
[1,3,4,5]


[1,2,3,4,5]
+6
[1,3,4,5]

+20
[1,3,4,5]



"""

class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
		#print(dp)
		nums = [1] + nums + [1]
		for length in range(1,n+1):
			for left in range(1, n-length+2):
				right = left + length - 1
				
				for k in range(left, right + 1):
					score = nums[left-1] * nums[k] * nums[right+1]
					#print(f'l:{left}, r:{right}, k:{k}')
					totalScore = score + dp[left][k-1] + dp[k+1][right]
					#print(f'l:{left}, r:{right}, k:{k}')
					dp[left][right] = max(dp[left][right], totalScore)
		#print(dp)
		return dp[1][n]
			
					























		