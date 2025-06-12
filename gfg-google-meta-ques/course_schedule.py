"""
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisites[][] tasks, for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return any one of them. If it is impossible to finish all tasks, return an empty array. Returning any correct order will give the output as true, whereas any invalid order will give the output false. 

Examples:

Input: n = 2, prerequisites[][] = [[1, 0]]
Output: true
Explanation: Only possible order is [0, 1].

Input: n = 4, prerequisites[][] = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: true
Explanation: There are a total of 4 tasks to pick. To pick task 3 you should have finished both tasks 1 and 2. Both tasks 1 and 2 should be pick after you finished task 0. So one correct task order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3]. Returning any of these order will result in an output of true.


"""
from collections import defaultdict, deque
class Solution:
  def findOrder(self, n, prerequisites):
    indeg = [0] * n
    adj = defaultdict(list)
    for idx in range(len(prerequisites)):
      [v, u] = prerequisites[idx]
      adj[u].append(v)
      indeg[v] += 1

    queue = deque()
    for idx in range(n):
      if indeg[idx] == 0:
        queue.append(idx)
    topo = []
    while queue:
      u = queue.popleft()
      topo.append(u)
      for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
          queue.append(v)

    return topo if len(topo) == n else []


#############################################################
from collections import defaultdict
class Solution:
  def findOrder(self, n, prerequisites):
    visited = [False] * n
    adj = defaultdict(list)
    for idx in range(len(prerequisites)):
      [v, u] = prerequisites[idx]
      adj[u].append(v)

    topo = []
    def dfs(u):
      for v in adj[u]:
        if visited[v]:
          continue
        visited[v] = True
        dfs(v)
      topo.append(u)

    for u in range(n):
      if visited[u]:
        continue
      visited[u] = True
      dfs(u)

    return topo[::-1] if len(topo) == n else []


