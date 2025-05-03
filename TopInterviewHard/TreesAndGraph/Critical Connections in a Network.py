"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.
"""
class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    vis = [0 for _ in range(n)]
    disc = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    critical = []
    timer = 0
    
    connect_map = dict()
    for (u,v) in connections:
      connect_map[u] = connect_map.get(u, []) + [v]
      connect_map[v] = connect_map.get(v, []) + [u]
    
    def dfs(node, parent):
      nonlocal timer
      vis[node] = 1
      low[node] = disc[node] = timer

      timer += 1

      for v in connect_map[node]:
        if v == parent:
          continue

        if vis[v] == 0:
          dfs(v,node)
          low[node] = min(low[node], low[v])
          if disc[node] < low[v]:
            critical.append((node,v))
        else:
          low[node] = min(low[node], low[v])

    dfs(0, -1)

    return critical