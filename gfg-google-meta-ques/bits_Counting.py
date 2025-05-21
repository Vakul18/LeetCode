"""
Given an integer n, return an array ans of size n + 1, where each element i (0 ≤ i ≤ n) represents the count of 1s in the binary form of i.

Input: n = 2
Output: [0, 1, 1]
Explanation:
0  --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0, 1, 1, 2, 1, 2] 
Explanation: 
0  --> 0 - 0
1 --> 1 - 1
2 --> 10 - 1
3 --> 11 - 2
4 --> 100 - 1
5 --> 101 - 2
6 --> 110 - 2
7 --> 111 - 3
8 --> 1000 - 1
9 --> 1001 - 2
10 --> 1010 - 2
11 --> 1011 - 3
12 --> 1100 - 2
13 --> 1101 - 3
14 --> 1110 - 3

0 1 1 2
1 2 2 3
1 2 2 3 2 3 3


x 



"""
from typing import List

class Solution:
  def countBits(self, n : int) -> List[int]:
    if n == 0:
      return [0]
    dp = [0]*(n+1)
    dp[1] = 1
    for num in range(2, n+1):
      dp[num] = dp[num>>1] + dp[(num & 1)]

    return dp














