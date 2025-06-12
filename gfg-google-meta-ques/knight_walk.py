"""
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.If it cannot reach the target position return -1.

Note:
The initial and the target position co-ordinates of Knight have been given accoring to 1-base indexing.

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:

Knight takes 3 step to reach from
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1). 

Example 2:

Input:
N=8
knightPos[ ] = {7, 7}
targetPos[ ] = {1, 5}
Output:
4
Explanation:
Knight takes 4 steps to reach from
(7, 7) to (1, 5):
(4, 5) -> (6, 5) -> (5, 3) -> (7, 2) -> (1, 5).
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the inital position of Knight (KnightPos), the target position of Knight (TargetPos) and the size of the chess board (N) as an input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position.If it cannot reach the target position return -1.

"""
from collections import deque

class Solution:
  def minStepToReachTarget(self, KnightPos, TargetPos, N):
    queue = deque([(KnightPos[0]-1, KnightPos[1]-1)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    target = (TargetPos[0]-1, TargetPos[1]-1)
    path = -1
    visited[KnightPos[0]-1][KnightPos[1]-1] = True
    while queue:
      size = len(queue)
      path+=1
      for i in range(size):
        new_pos = queue.popleft()
        
        if new_pos == target:
          found = True
          return path
        
        
        neis = [(1,2), (2,1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-2, -1), (-1, -2)]

        for dx, dy in neis:
          x = new_pos[0] + dx
          y = new_pos[1] + dy

          if x < 0 or x >= N or y < 0 or y>= N or visited[x][y]:
            continue
          visited[x][y] = True
          queue.append((x, y))

    return -1  
      
        














