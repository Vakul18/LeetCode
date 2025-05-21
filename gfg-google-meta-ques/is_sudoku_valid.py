"""
Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix(mat[][]) the task to check if the current configuration is valid or not where a 0 represents an empty block.
Note: Current valid configuration does not ensure validity of the final solved sudoku. 

Examples:

Input: mat[][] = [
[3, 0, 6, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: true
Explaination: It is possible to have aproper sudoku.
Input: mat[][] = [
[3, 0, 3, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: false
Explaination: It is not possible to have aproper sudoku.
Input: mat[][] = [
[2, 0, 2, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: false
Explaination: It is not possible to have aproper sudoku.


 0  1  2  3  4  5  6  7  8
[2, 0, 2, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45


1. create a 9+9 sets of rows and cols. check for duplicates.
2. create 9 sets of blocks, maintain a counter c%3, r%3 for getting block canonical form and add it to arr of sets.
"""
class Solution:
  def isValid(self, mat):
    row = [[False] * 10 for _ in range(9)]
    col = [[False] * 10 for _ in range(9)]
    block = [[False] * 10 for _ in range(9)]
    
    for i in range(9):
      for j in range(9):
        val = mat[i][j]
        if val == 0:
          continue
        if row[i][val]:
          return False
        else:
           row[i][val] = True

        if col[j][val]:
          return False
        else:
           col[j][val] = True

        block_idx = i//3*3 + j//3

        if block[block_idx][val]:
          return False
        else:
           block[block_idx][val] = True

    return True
       

 

    
    


















