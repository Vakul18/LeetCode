"""
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u,v] represents the edge between the vertices u and v. Determine whether a specific edge between two vertices (c, d) is a bridge.

Note:

An edge is called a bridge if removing it increases the number of connected components of the graph.
if there’s only one path between c and d (which is the edge itself), then that edge is a bridge.

|---|
| 3-4 
| |
0-1-2
|___|


"""

from collections import defaultdict
class Solution:
  def isBridge(self, V, edges, c, d):
    id = [-1] * V
    low = [-1] * V
    timer = 0
    adj = defaultdict(list)
 
    for edge in edges:
      adj[edge[0]].append(edge[1])
      adj[edge[1]].append(edge[0])
 
    bridges = []

    def findBridge(node, parent):
      nonlocal timer
      id[node], low[node] = timer, timer
      timer += 1

      for v in adj[node]:
        if v == parent:
          continue

        if id[v] == -1:
          findBridge(v, node)
          low[node] = min(low[node], low[v])
          
          if low[node] < low[v]:
            bridges.append((node, v))

        else:
          low[node] = min(low[node], low[v])
      
    
    for u in range(V):
      if id[u] != -1:
        continue

      findBridge(u, -1)

    return True if (c,d) in bridges or (d, c) in bridges else False

    