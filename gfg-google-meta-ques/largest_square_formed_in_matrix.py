"""
Given a binary matrix mat, find out the maximum length of a side of a square sub-matrix with all 1s.

Input: mat = [[0, 1, 1, 0, 1], 
              [1, 1, 0, 1, 0],
              [0, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0]]
Output: 3
"""


from typing import List


class Solution:
  def maxSquare(self, mat):
    n, m = len(mat), len(mat[0])
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    for i  in range(n):
      dp[i][0] = mat[i][0]
      max_side = max(dp[i][0], max_side)

    for i  in range(m):
      dp[0][i] = mat[0][i]
      max_side = max(dp[0][i], max_side)

    for i in range(1, n):
      for j in range(1, m):
        if mat[i][j] == 1:
          dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
          max_side = max(dp[i][j], max_side)
        else:
          dp[i][j] = 0
       
    return max_side
