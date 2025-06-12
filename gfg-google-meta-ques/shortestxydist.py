"""
Given a N*M grid of characters 'O', 'X', and 'Y'. Find the minimum Manhattan distance between a X and a Y.

Manhattan Distance :
| row_index_x - row_index_y | + | column_index_x - column_index_y |

Input:
N = 4, M = 4
grid  = {{X, O, O, O}
         {O, Y, O, Y}
         {X, X, O, O}
         {O, Y, O, O}}
Output:
1
Explanation:
{{X, O, O, O}
{O, Y, O, Y}
{X, X, O, O}
{O, Y, O, O}}
The shortest X-Y distance in the grid is 1.
One possible such X and Y are marked in bold
in the above grid.
Example 2:

Input:
N = 3, M = 3
grid = {{X, X, O}
        {O, O, Y}
        {Y, O, O}}
Output :
2
Explanation:
{{X, X, O}
 {O, O, Y}
 {Y, O, O}}
The shortest X-Y distance in the grid is 2.
One possible such X and Y are marked in bold
in the above grid.
"""
#User function Template for python3

class Solution:
  def shortestXYDist(self, grid, N, M):
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]
    min_path = float('inf')
    for i in range(N):
      for j in range(M):
        if grid[i][j] == 'X':
          dist[i][j] = 0
        else:
          if j > 0:
            dist[i][j] = dist[i][j-1] + 1
          if i > 0:
            dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)

    for i in range(N-1, -1, -1):
      for j in range(M-1, -1, -1):
        if grid[i][j] == 'X':
          dist[i][j] = 0
        else:
          if j < M-1:
            dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
          if i < N -1:
            dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)

        if grid[i][j] == 'Y':
          min_path = min(min_path, dist[i][j])

    return min_path

    
          








    