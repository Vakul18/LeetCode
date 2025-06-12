"""
given a matrix, find max path that can be traversed from the given point. assume traversal is always done in optmized way.

in the matrix O represents walkable path and X represents obstacles.

o o o o
o o o o
o o x o
o r x o

"""
from collections import deque

def find_max_path(grid : list[list[int]], start_pt : tuple[int, int]) -> int:
  visited = set([start_pt])
  path_len = 0
  queue = deque([start_pt])
  m, n = len(grid), len(grid[0])

  while queue:
    size = len(queue)
    for _ in range(size):
      i, j = queue.popleft()
      for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + dx, j + dy
        if ni < 0 or ni >= m or nj < 0 or nj >= n or ((ni, nj) in visited) or grid[ni][nj] == 'x':
          continue
        visited.add((ni, nj))
        queue.append((ni, nj))

    path_len += 1     
 

  return path_len


matrix = [
    ['o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o'],
    ['o', 'o', 'x', 'o'],
    ['o', 'o', 'x', 'o']
]

start = (3, 1)
print(find_max_path(matrix, start))  # Output: 10
