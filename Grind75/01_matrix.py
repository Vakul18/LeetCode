"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

m*n matrix

visited : m*n
queue : (i,j)

5 4 3
1 1 2
2 1 1
1 1 0

given indices i,j find nearest 0

find all zeroes
do bfs from each zero and update cell values which are not zero.
we can check min value of the cell and current value and update it to min.
we will need to maintain visited to know whether a 1 is updated value or original.
"""
from collections import deque
import math
class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		m = len(mat)
		n = len(mat[0])
		dist_mat = [[float('inf')] * n for _ in range(0, m)]
		queue = deque([])
		for i in range(0, m):
			for j in range(0,n):
				if mat[i][j] == 0:
					queue.append((i,j))
					dist_mat[i][j] = 0
		
		while queue:
			idx = queue.popleft()
			neighbours = [(-1, 0), (1,0), (0,-1), (0,1)]
			idx_val = dist_mat[idx[0]][idx[1]]
			for neighbour in neighbours:
				nei_idx = (idx[0]+neighbour[0], idx[1] + neighbour[1])
				if nei_idx[0] < 0 or nei_idx[0] >= m or nei_idx[1] < 0 or nei_idx[1] >= n  or dist_mat[nei_idx[0]][nei_idx[1]] != float('inf'):
					continue
				dist_mat[nei_idx[0]][nei_idx[1]] = min(idx_val + 1, dist_mat[nei_idx[0]][nei_idx[1]])	
				queue.append(nei_idx)

		return dist_mat



class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(mat), len(mat[0])

        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] != 0:
                    top = mat[r - 1][c] + 1 if r > 0 else float("inf")
                    left = mat[r][c - 1] + 1 if c > 0 else float("inf")
                    mat[r][c] = min(top, left)
        
        for r in range(n_rows - 1, -1, -1):
            for c in range(n_cols - 1, -1, -1):
                if mat[r][c] > 1:
                    bot = mat[r + 1][c] + 1 if r + 1 < n_rows else float("inf")
                    right = mat[r][c + 1] + 1 if c + 1 < n_cols else float("inf")
                    mat[r][c] = min(mat[r][c], bot, right)
        
        return mat






		