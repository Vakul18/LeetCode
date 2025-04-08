"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


start : 0,0


"""

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    visited = set()
    m = len(board)
    n = len(board[0])
    def bk(i,j, idx):
      if board[i][j] != word[idx]:
        return False
      if idx == len(word) - 1:
        return True
      visited.add((i,j))
      d = [(1,0), (-1,0), (0,1), (0,-1)]

      for dr,dc in d:
        r,c = i + dr, j + dc
        if r < 0 or c < 0 or r >= m or c >= n or ((r,c) in visited):
          continue
        result = bk(r,c,idx + 1)
        if result:
          return True
      visited.remove((i,j))
      return False

    for i in range(m):
      for j in range(n):
        if bk(i,j,0):
          return True
    return False


-----------------------------------------------------------------------------------

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, k = len(board[0]), len(board), len(word)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for i in range(n):
            for j in range(m):
                freq1[board[i][j]] += 1
        for ch in word:
            freq2[ch] += 1
        for key, val in freq2.items():
            if freq1[key] < val:
                return False
        if freq2[word[0]] > freq2[word[-1]]:
            word = word[::-1]


        def dfs(i, j, pos):
            if pos == k - 1:
                return True
            temp = board[i][j]
            board[i][j] = ""
            for d in directions:
                i_, j_ = i + d[0], j + d[1]
                if 0 <= i_ < n and 0 <= j_ < m and board[i_][j_] == word[pos+1]:
                    if dfs(i_, j_, pos + 1): return True
            board[i][j] = temp
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0): return True
        return False
