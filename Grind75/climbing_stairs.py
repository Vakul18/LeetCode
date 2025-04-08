"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

n = 2, 1+1, 2 -> 2

n = 3, 1+1+1, 1+2, 2+1 -> 3

n = 4, 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 -> 5

no. of 2s = 2

dp [0-n]

dp[0] = 0

dp[i] = dp[i-1] + dp[i-2]
n = 4

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
"""
class Solution:
  def climbStairs(self, n: int) -> int:
    if n == 1:
      return 1
    if n == 2:
      return 2

    dp = [0]*(n+1)

    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
      dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
      