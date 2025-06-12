"""
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 
"""
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0] * n

  def find_parent(self, x):
    if self.parent[x] == x:
      return x
    root = x
    while self.parent[root] != root:
      root = self.parent[root]

    while self.parent[x] != x:
      parent = self.parent[x]
      self.parent[x] = root
      x = parent
      
    return root

  def union(self, x, y):
    px, py = self.find_parent(x), self.find_parent(y)
    if px == py:
      return

    if self.rank[px] > self.rank[py]:
      self.parent[py] = px
    else:
      self.parent[px] = py
      if self.rank[px] == self.rank[py]:
        self.rank[py] += 1

class Solution:
  def minDays(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def get_idx(i, j, n):
      return i*n + j

    def count_islands():
      m, n = len(grid), len(grid[0])
      uf = UnionFind(m*n)
      land_cells = []

      for i in range(m):
        for j in range(n):
          if grid[i][j] == 1:
            idx = get_idx(i, j, n)
            land_cells.append(idx)

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
              ni, nj = i + dx, j + dy
              n_idx = get_idx(ni, nj, n)
              if ni >= 0 and ni < m and nj >=0 and nj < n and grid[ni][nj] == 1:
                uf.union(idx, n_idx)

   
      roots = set()
      for cell in land_cells:
        roots.add(uf.find_parent(cell))

      return len(roots)        
              

    island_count = count_islands()
    if island_count != 1:
      return 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          continue
        grid[i][j] = 0 # disconnect
        count = count_islands()
        if count != 1:
          return 1
      
        grid[i][j] = 1

    return 2



      

    
    
    
        