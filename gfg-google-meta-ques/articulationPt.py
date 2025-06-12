"""
You are given an undirected graph with V vertices and E edges. The graph is represented as a 2D array edges[][], where each element edges[i] = [u, v] indicates an undirected edge between vertices u and v.
Your task is to return all the articulation points (or cut vertices) in the graph.
An articulation point is a vertex whose removal, along with all its connected edges, increases the number of connected components in the graph.

Note: The graph may be disconnected, i.e., it may consist of more than one connected component.
If no such point exists, return {-1}.

|---|
| 3-4 
| |
0-1-2
|___|




    3-4-6 
    |
5-0-1-2
  |___|


  3-4 
  |
0-1-2

"""
from collections import defaultdict
class Solution:
  def articulationPoints(self, V, edges):
    id = [-1] * V
    low = [-1] * V
    timer = 0
    mark = [False] * V
    adj = defaultdict(list)

    def findAP(node, parent):
      nonlocal timer
      id[node] = low[node] = timer
      timer += 1
      child = 0
      for v in adj[node]:
        if v == parent:
          continue

        if id[v] == -1:
          child += 1
          findAP(v, node)

          low[node] = min(low[node], low[v])

          if id[node] <= low[v] and parent != -1:
            mark[node] = True
        else:
          low[node] = min(low[node], id[v])
      if parent == -1 and child > 1:
        mark[node] = True 


    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    for v in range(V):
      if id[v] != -1:
        continue
      findAP(v, -1)
       
    
    aps = []
    for v in range(V):
      if mark[v]:
        aps.append(v)

    return aps if len(aps) > 0 else  [-1]