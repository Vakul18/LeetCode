"""
Given a 2-D binary matrix of size n*m, where 0 represents an empty space while 1 represents a wall you cannot walk through. You are also given an integer k.
You can walk up, down, left, or right. Given that you can remove up to k walls, return the minimum number of steps to walk from the top left corner (0, 0) to the bottom right corner (n-1, m-1).
Note: If there is no way to walk from the top left corner to the bottom right corner, return -1.


Example 1:

Input: n = 3, m = 3, k = 1
mat = {{0, 0, 0},
       {0, 0, 1},
       {0, 1, 0}}
Output:
4
Explanation:
We can remove any one of the walls and
reach the bottom in 4 moves.  
Example 2:

Input:
n = 2, m = 2, k = 0
mat[] = {{0, 1},
         {1, 0}}
Output:
-1
Explanation:
There's no way of reaching the bottom
corner without removing any walls.

Your Task:
The task is to complete the function shotestPath() which takes three integers n, m, and k and also a matrix of size n*m as input and returns the minimum number of steps to walk from the top left corner to the bottom right corner.


Constraints:
1 ≤ n,m ≤ 50
0 ≤ k ≤ n*m
Top left and bottom right corners doesn't have 1


Expected Time Complexity: O(n*m*k).
Expected Auxiliary Space: O(n*m*k).
"""

#User function Template for python3
from collections import deque
class Solution:
  def shotestPath(self, grid, n, m, k):
    queue = deque([(0,0,0)])
    path_len = -1
    visited = [[[False, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][0], visited[0][0][1] = True, 0   
    
    while queue:
      path_len += 1
      size = len(queue)
      
      for _ in range(size):
        x, y, walls = queue.popleft()

      
        if x == n-1 and y == m-1:
          return path_len

        neighbours = [(1,0), (0,1), (-1,0), (0,-1)]

        for dx,dy in neighbours:
          x_n = x + dx
          y_n = y + dy

          if x_n < 0 or x_n >= n or y_n < 0 or y_n >= m or (grid[x_n][y_n] + walls) > k or (visited[x_n][y_n][0] and visited[x_n][y_n][1] <= (grid[x_n][y_n] + walls)):
            continue

          if x_n == n-1 and y_n == m-1:
            return path_len + 1

          visited[x_n][y_n][0] = True
          visited[x_n][y_n][1] = grid[x_n][y_n] + walls
          queue.append((x_n, y_n, grid[x_n][y_n] + walls))

        

    return -1






















