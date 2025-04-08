"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

1. start from top left
2. traver right and bottom using dfs till 0s are found.
3. Mark all visited cells as 1.
4. count 1 for 1 dfs cycle.
5. apple dfs for whole m*n matrix.

"""
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    num_of_islands = 0
    
    for i in range(m):
      for j in range(n):
        if visited[i][j] or grid[i][j] == '0':
          continue

        stack = [(i, j)]
        visited[i][j] = True
        
        while stack:
          x, y = stack.pop()
          
          # Check all 4 directions (up, down, left, right)
          directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
          for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
              visited[nx][ny] = True
              stack.append((nx, ny))
        
        num_of_islands += 1

    return num_of_islands




        

        
        
