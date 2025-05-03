"""
Given an undirected graph with V vertices and adjacency list adj. Find all the vertices removing which (and edges through it) would increase the number of connected components in the graph. The graph may be initially disconnected.. Return the vertices in ascending order. If there are no such vertices then returns a list containing -1.
"""
class Solution:
    
  #Function to return Breadth First Traversal of given graph.
  def articulationPoints(self, n, adj):
    vis = [False for _ in range(n)]
    disc = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    art_points = set()
    timer = 0
    
    def dfs(node, parent):
      nonlocal timer
      low[node] = disc[node] = timer
      timer += 1
      vis[node] = True
      child = 0
      for v in adj[node]:
        if v == parent:
          continue
        if vis[v]:
          low[node] = min(low[node], disc[v])
        else:
          child += 1
          dfs(v, node)
          low[node] = min(low[node], low[v])
          if low[v] >= disc[node] and parent != -1:
            art_points.add(node)
      if parent == -1 and child > 1:
        art_points.add(node)
        
    for pt in range(n):
      if not vis[pt]:
        dfs(pt, -1)
    return sorted(art_points) if art_points else [-1]
        