"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


p = [100, 5,20, 9, 80,25,40,109]
pr = 
(1,7) : 104






"""

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		dp = [[-1,-1] for _ in range(n)]
		
		return self.get_max_profit(prices, dp, 0, 0)

	def get_max_profit(self, prices, dp, idx, buy):
		if idx >= len(prices):
			return 0
		if dp[idx][buy] != -1:
			return dp[idx][buy]

		result = float('-inf')
		if buy == 1:
			result = max(self.get_max_profit(prices, dp, idx+1, 1), (prices[idx] + self.get_max_profit(prices, dp, idx+2, 0)))	
		
		else:
			result = max(self.get_max_profit(prices, dp, idx+1, 0), (-prices[idx] + self.get_max_profit(prices, dp, idx+1, 1)))

		dp[idx][buy] = result

		return result	





def stock_profit(prices):
    n = len(prices)
    
    # Create a 2D dp array of size [n+2][2] initialized to 0
    dp = [[0 for _ in range(2)] for _ in range(n + 2)]

    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0

            if buy == 0:  # We can buy the stock
                profit = max(
                    0 + dp[ind + 1][0],
                    -prices[ind] + dp[ind + 1][1]
                )

            if buy == 1:  # We can sell the stock
                profit = max(
                    0 + dp[ind + 1][1],
                    prices[ind] + dp[ind + 2][0]
                )

            dp[ind][buy] = profit

    return dp[0][0]



