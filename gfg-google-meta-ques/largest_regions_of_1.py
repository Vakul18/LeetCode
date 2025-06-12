"""
Unit Area of largest region of 1's

Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).
 

Example 1:

Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
Output: 5
Explanation: The grid is-
1 1 1 0
0 0 1 0
0 0 0 1
The largest region of 1's is colored
in orange.
Example 2:

Input: grid = {{0,1}}
Output: 1
Explanation: The grid is-
0 1
The largest region of 1's is colored in 
orange.
"""
class Solution:
  def findMaxArea(self, grid):
    max_area = 0
    m, n = len(grid[0]), len(grid)
    visited = [[False for _ in range(m)] for _ in range(n)]
   
    def search(i, j):
      nonlocal n, m
      visited[i][j] = True
      dxs = [-1, 0, 1]
      dys = [-1, 0, 1]
      area = 1
      for dx in dxs:
        for dy in dys:
          x, y = i + dx, j + dy
          if (dx == 0 and dy == 0) or x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0 or visited[x][y]:
            continue

          area += search(x, y)

      return area        
   
    for i in range(n):
      for j in range(m):
        if visited[i][j] or grid[i][j] == 0:
          continue
        max_area = max(max_area, search(i, j))

    return max_area
############################################################################################


from collections import deque
class Solution:
    
    #Function to check whether the cell is within the matrix bounds.
    def isValid(self, x, y, n, m):
        return (x >= 0 and x < n and y >= 0 and y < m)
    
    
    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        #these lists are used to get row and column numbers
        #of 8 neighbours of a given cell.
        dx = [-1,1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        
        #queue to store the cell indexes which have grid value 1.
        q = deque()
        ans = 0
        
        #traversing all the cells of the matrix.
        for i in range(n):
            for j in range(m):
                
                #if grid value is 1, we update the grid value as 0 
			    #and push the cell indexes into queue.
                if(grid[i][j] == 1):
                    cnt =  1
                    grid[i][j] =  0
                    q.append([i,j])
                    
                    
                    while(len(q)):
                        
                        #storing the cell indexes at top of 
                        #queue and popping them.
                        cur = q.popleft()
                        x = cur[0]
                        y = cur[1]
                        
                        #iterating over the adjacent cells.
                        for k in range(8):
                            n_x = x + dx[k]
                            n_y = y + dy[k]
                            
                            #if indexes are within range and grid value is 1,
                            #we update the grid value as 0, increment counter 
			                #and push the cell indexes into queue.
                            if(self.isValid(n_x,n_y,n,m) and grid[n_x][n_y]==1):
                                cnt = cnt + 1
                                grid[n_x][n_y] = 0
                                q.append([n_x, n_y])
                                
                    #updating maximum area.
                    ans = max(ans, cnt)
        
        return ans
    