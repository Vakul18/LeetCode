"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

2 3 4
8 9 1
1 3 7
 

"""

class Solution:

	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
		self.matrix = matrix
		self.maxRow = len(matrix)
		self.maxCol = len(matrix[0])
		self.pathLenMem = [[-1] * self.maxCol for _ in range(self.maxRow)]
		
		maxPathLen = 1
		for rowIdx in range(self.maxRow):
			for colIdx in range(self.maxCol):
				maxPathLen = max(maxPathLen, self.searchPath(rowIdx, colIdx))
		
		return maxPathLen


	def searchPath(self, rowIdx : int, colIdx: int) -> int:
		
		if self.pathLenMem[rowIdx][colIdx] != -1:
			return self.pathLenMem[rowIdx][colIdx]

		offsets = [(0,-1), (0,1), (1,0), (-1,0)]
		
		currPathLen = 1
		for offset in offsets:
			neighbourRowIdx, neighbourColIdx  = rowIdx + offset[0], colIdx + offset[1]
			if self.isValidCell(neighbourRowIdx, neighbourColIdx)  and (self.matrix[rowIdx][colIdx] < self.matrix[neighbourRowIdx][neighbourColIdx]):
				currPathLen = max(currPathLen, 1 + self.searchPath(neighbourRowIdx, neighbourColIdx))

		self.pathLenMem[rowIdx][colIdx] = currPathLen
		
		return currPathLen

	def isValidCell(self, rowIdx, colIdx):
		if rowIdx >= self.maxRow or rowIdx < 0 or colIdx >= self.maxCol or colIdx < 0:
			return False
		return True

