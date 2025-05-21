"""
Find kth element of spiral matrix

Given a matrix with n rows and m columns. Your task is to find the kth element which is obtained while traversing the matrix spirally. You need to complete the method findK which takes four arguments the first argument is the matrix A and the next two arguments will be n and m denoting the size of the matrix A and then the forth argument is an integer k. The function will return the kth element obtained while traversing the matrix spirally.

n = 4, m = 4, k = 10
A[][] = {{1  2  3  4},
         {5  6  7  8},
         {9  10 11 12},
         {13 14 15 16}}

4x4 -> < 2x2
00, 11, 22*

a[][] = 1 2 3 1
        4 5 6 1
        7 8 9 1

3x4 = < 1x2
00, 11, 22*

a[][] = 1 2 3 4
        5 6 7 8

2x4 -> < 1x2

1. check in which spiral does k lie
2. check elements in spiral
3. 1st spiral: 2*m + n - 2
4. 2nd spiral: 2*(m-2) + (n-2) - 2
4. 3rd spiral: 2*(m-4) + (n-4) - 2


a[][] = 1 2 3 4
        5 6 7 8

k = 7

"""
#User function Template for python3

class Solution:
  def findK(self, a, n, m, k):
    r, c = n, m
    count = 0
    """
    k = 7
    count = 0
    r = 2, c = 4

    """
    start_pt = [0, 0]
    while r >= 0 and c >=0:
      """
      count = 4
      i = 0, j 0 -> 4
      """
      # top row
      i = start_pt[0]
      for j in range(start_pt[1], c + start_pt[1]):
        count += 1
        if count == k:
          return a[i][j]

      # right column
      j = start_pt[1] + c - 1
      for i in range(start_pt[0] + 1, r + start_pt[0]):
        count += 1
        if count == k:
          return a[i][j]

      # bottom row
      i = start_pt[0] + r - 1
      for j in range(c + start_pt[1] - 2, start_pt[1] - 1, -1):
        count += 1
        if count == k:
          return a[i][j]

      # left column
      j = start_pt[1]
      for i in range(r + start_pt[0] - 2, start_pt[0], -1):
        count += 1
        if count == k:
          return a[i][j]
        
      r = r - 2
      c = c - 2
      start_pt = [start_pt[0]+1, start_pt[1]+1]

  
    return -1













