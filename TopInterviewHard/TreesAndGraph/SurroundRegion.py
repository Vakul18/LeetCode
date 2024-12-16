"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

X X X X
X O O X
X X X O

O X X O X
X O O X O
X O X O X
O X O O O
X X O X O


[["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","X","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
[["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

"""
from collections import deque
class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
        
		oFreeSlots = set()
		stack = deque()
	
		m = len(board)
	
		if m == 0:
			return

		n = len(board[0])

		if m <= 2 or n <= 2:
			return

		for i in [0,m-1]:
			for j in range(0, n):
				if board[i][j] == 'O':
					stack.append((i,j))
					oFreeSlots.add((i,j))


		for i in range(1,m-1):
			for j in [0,n-1]:
				if board[i][j] == 'O':
					stack.append((i,j))
					oFreeSlots.add((i,j))

		
		#print('1')
		#print(oFreeSlots)
		while stack:
			(i,j) = stack.pop()
			#print(f'loop : {(i,j)}')
			offsets = [[-1,0], [1,0], [0,-1], [0,1]]
			for offset in offsets:
				currIndex = (i + offset[0], j + offset[1])
				if (currIndex[0]<0 or currIndex[0]>=m) or (currIndex[1]<0 or currIndex[1]>=n) or (currIndex in oFreeSlots):
					continue
			
				if board[currIndex[0]][currIndex[1]] == 'O':
					oFreeSlots.add(currIndex)
					stack.append(currIndex)
		
		#print('2')
		#print(oFreeSlots)

		for i in range(1,m-1):
			for j in range(1,n-1):
				if (board[i][j] == 'O') and ((i,j) not in oFreeSlots):
					board[i][j] = 'X'
	
		return
 		

O X X O X
X O O X O
X O X O X
O X O O O
X X O X O

00 03 42 44
30 14 34




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # mark areas that cannot be captured, aka o's on boundary
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][n-1] == 'O':
                self.dfs(i, n - 1, board)
        
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[m-1][j] == 'O':
                self.dfs(m - 1, j, board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def dfs(self, row, col, board):
        m, n = len(board), len(board[0])
        if row < 0 or col < 0 or row >=m or col >= n or board[row][col] != 'O':
            return
        board[row][col] = '#'
        self.dfs(row+1, col, board)
        self.dfs(row-1, col, board)
        self.dfs(row, col+1, board)
        self.dfs(row, col-1, board)



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def dfs(i, j):
            # Check boundaries and whether the cell is 'O'
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            # Mark the cell as safe
            board[i][j] = '#'
            
            # Explore all four directions
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        # Step 1: Mark all 'O's connected to the boundary as safe
        for i in range(m):
            if board[i][0] == 'O':  # Left boundary
                dfs(i, 0)
            if board[i][n - 1] == 'O':  # Right boundary
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':  # Top boundary
                dfs(0, j)
            if board[m - 1][j] == 'O':  # Bottom boundary
                dfs(m - 1, j)
        
        # Step 2: Flip all remaining 'O's to 'X' and '#' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Capture surrounded regions
                elif board[i][j] == '#':
                    board[i][j] = 'O'  # Restore safe regions

