"""
Given a matrix mat where every element is either 'O' or 'X'. Replace all 'O' or a group of 'O' with 'X' that are surrounded by 'X'.

A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above, just left and just right of it.
"""

class Solution:
  def fill(self,  mat):
    m, n = len(mat), len(mat[0])
 
    # check boundary Os
    boundary_coords = []
    for r in [0, m-1]:
      for c in range(n):
        if mat[r][c] == 'O':
          mat[r][c] = 'B'
          boundary_coords.append((r, c))

    for r in range(m):
      for c in [0, n-1]:
        if mat[r][c] == 'O':
          mat[r][c] = 'B'
          boundary_coords.append((r, c))

     
    while boundary_coords:
      r, c = boundary_coords.pop()
      neighbours = [(-1,0), (0,-1), (1, 0), (0, 1)]

      for neighbour in neighbours:
        coord = (r + neighbour[0], c + neighbour[1])

        if coord[0] < 0 or coord[1] < 0 or coord[0] >= m or coord[1] >= n:
          continue 

        if mat[coord[0]][coord[1]] == 'O':
          mat[coord[0]][coord[1]] = 'B'
          boundary_coords.append(coord)

    for r in range(m):
      for c in range(n):
        if mat[r][c] == 'O':
          mat[r][c] = 'X'
        elif mat[r][c] == 'B':
          mat[r][c] = 'O'

    return mat