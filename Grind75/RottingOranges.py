"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


0  1 0
0 -1 0
0  0 0 

|
1

set of fresh oranges
queue : indices of fresh oranges
iterate all matrix and fill queue
maintain time for till elements in the queue are processed,
then add the new rotten oragens to the queue and remove from fresh oranges set and process again
return total time.

"""
from collections import deque
class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		fresh_oranges = set()
		rotten_oranges = deque()

		n = len(grid)
		m = len(grid[0])

		for i in range(0,n):
			for j in range(0,m):
				if grid[i][j] == 1:
					fresh_oranges.add((i,j))
				elif grid[i][j] == 2:
					rotten_oranges.append((i,j))
		time = 0
		neighbours = [(-1,0),(0,-1), (1,0), (0,1)]
		while len(fresh_oranges) > 0:
			new_rotten_oranges = set()
			while rotten_oranges:
				rotten_orange = rotten_oranges.pop()
				for neighbour in neighbours:
					r = rotten_orange[0] + neighbour[0]
					c = rotten_orange[1] + neighbour[1]
					
					if r >= 0 and r < n and c >=0 and c < m and grid[r][c] == 1:
						new_rotten_oranges.add((r,c))
		
			
			for rotten_orange in new_rotten_oranges:
				grid[rotten_orange[0]][rotten_orange[1]] = 2
				fresh_oranges.remove((rotten_orange[0], rotten_orange[1]))
				rotten_oranges.append((rotten_orange[0], rotten_orange[1]))
			if not rotten_oranges:
				return -1
			time += 1
		return time
				


#################################

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = [[-1] * n for _ in range(m)]
        
        q = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append(([row, col], 0))
                    seen[row][col] = 2

        time = 0

        while q:
            curr, t = q.popleft()
            row , col = curr
            time = max(t, time)

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nrow, ncol = row + dr, col + dc

                if nrow >= 0 and ncol >= 0 and nrow < m and ncol < n and grid[nrow][ncol] == 1 and seen[nrow][ncol] != 2:
                    q.append(([nrow, ncol], t + 1))
                    seen[nrow][ncol] = 2
        
        count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and seen[row][col] != 2:
                    count += 1
        
        return -1 if count else time





        
        


        
			 
				
			
	
		