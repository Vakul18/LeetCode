"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1



"""
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf') for _ in range(amount+1)]

    dp[0] = 0	

    for curr_amount in range(1, amount+1):
      for coin in coins:
        if curr_amount - coin >=  0:
          dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount-coin])

    return dp[amount] if not math.isinf(dp[amount]) else -1




