"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

12

dp [0,inf,inf, inf, inf,inf,inf,inf,inf,inf,inf,inf,inf]



"""
import math

class Solution:
	def numSquares(self, n: int) -> int:
		dp = [float('inf')] * (n+1)
		
		dp[0] = 0

	
		for i in range(1,n+1):
			for j in range(1, int(math.sqrt(i))+1) :
				dp[i] = min(dp[i],1 + dp[i - j*j])

		return dp[n]
			