"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

9 rows, 9 cols, 9 cells of 3*3

00, 01, 02  0 
10, 11, 12
20, 21, 22

03, 04, 05 1
13, 14, 15
23, 24, 25

06, 07, 08 2
16, 17, 18
26, 27, 28

                 
30, 31, 32 3
40, 41, 42
50, 51, 52

60 2+4

90 3
8,8

"""
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)] 
    box_sets = [set() for _ in range(9)]

    for i in range(9):
      for j in range(9):
        if board[i][j] == '.':
          continue

        if board[i][j] in row_sets[i] or board[i][j] in col_sets[j] or board[i][j] in box_sets[(i//3)*3 + (j//3)]:
          return False
        row_sets[i].add(board[i][j])
        col_sets[j].add(board[i][j])
        box_sets[(i//3)*3 + (j//3)].add(board[i][j])

    return True
    
        