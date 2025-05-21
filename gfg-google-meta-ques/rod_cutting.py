"""
Given a rod of length n inches and an array price[], where price[i] denotes the value of a piece of length i. Your task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: n = size of price, and price[] is 1-indexed array.


Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.
Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1] = 8*3 = 24.
Input: price[] = [3]
Output: 3
Explanation: There is only 1 way to pick a piece of length 1.

n
(1, n-1)
   /         \         \
(1, n-2)     (2, n-3)  (4, n-5)
  /     \
(3, n-5)


dp[i] : 1 -> n 


1,1,1,1    2,1,1    3,1             | 10
1,1,1,1,1  2,1,1,1  3,1,1 3,2  4,1 


1 5 8 9 10 17 17 20

0 1 5 8 9 10 17 17 20

"""
#User function Template for python3

class Solution:
  def cutRod(self, price):
    n = len(price)
    dp = [0] * (n+1)
    for i in range(1, n+1):
      dp[i] = price[i-1]
       
    
    for i in range(1, n+1):
      for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

    return dp[n]




