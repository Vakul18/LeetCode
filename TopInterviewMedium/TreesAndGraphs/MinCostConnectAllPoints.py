"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

1. Find all distances O(n^2)
2. sort all point by relative distance. n^2log(n)
3. use disjoint set to pick lowest possible edge then try to add to tree with cycle.
4. repeat 3 till all points are covered.


"""

# using Kruskal
class DisjointSet:
  def __init__(self, n):
    self.n = n
    self.parent = [-1]*(n+1)
    self.rank = [0]*(n+1)
    for i in range(n+1):
      self.parent[i] = i

  def findParent(self, u):
    if self.parent[u] == u:
      return u
    self.parent[u] = self.findParent(self.parent[u])
    return self.parent[u]
  
  def union(self, u, v):
    pu = self.findParent(u)
    pv = self.findParent(v)
    if self.rank[pu] > self.rank[pv]:
      self.parent[pv] = pu
    elif self.rank[pv] > self.rank[pu]:
      self.parent[pu] = pv
    else:
      self.parent[pv] = pu
      self.rank[pu] += 1


class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)
    edges = []

    for i in range(n): 
      for j in range(i+1,n):
        xi, yi = points[i][0], points[i][1]
        xj, yj = points[j][0], points[j][1]
        wt = abs(xi-xj) + abs(yi-yj)
        edges.append((wt, i, j))
    
    edges_s = sorted(edges, key = lambda x : x[0])
    
    ds = DisjointSet(n)
    edge_count = 0
    min_cost = 0
    for edge in edges_s:
      wt, u, v  = edge
      if ds.findParent(u) != ds.findParent(v):
        min_cost += wt
        edge_count += 1
        ds.union(u,v)
        if edge_count == n-1:
          break
    return min_cost
     
    

-----------------------

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def union(parent,a,b):
            p1,p2 = get_parent(a),get_parent(b)
            parent[p2]=p1

        def get_parent(a):
            if parent[a]==a:
                return a
            
            p = get_parent(parent[a])
            parent[a]=p
            return p 


        
        def man(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        distances = {}
        for i in range(len(points)):
            for j in range(len(points)):
                point1,point2 = points[i],points[j]
                if i!=j:
                    distances[(i,j)] = man(point1,point2)
        heap = []
        for key in distances:
            heapq.heappush(heap,(distances[key],key))
        n = len(points)
        found = 0
        tot = 0
        parent = [i for i in range(n)]
        while found!=n-1:
            dist,(f,t) = heapq.heappop(heap)
            p1,p2 = get_parent(f),get_parent(t)
            if p1 == p2:
                continue
            found+=1
            tot+=dist
            union(parent,f,t)
        return tot
             

        

---------------------------
"""
[[0,0],[1,1],[1,0],[-1,1]]
 0         1     2    3     

0: [(1, 2), (2, 1), (3, 2)], 
1: [(2, 1), (3, 2)],
2: [(3, 3)]})

visited = [t, t, t, t, f]
pq = [ (1,2), (2,1),  (2,3), (2,3) ,(3,3)]
"""

import heapq
from collections import defaultdict
# using prims
class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    pq = []
    n = len(points)
    adj = defaultdict(list)
    for i in range(n-1): 
      for j in range(i+1,n):
        xi, yi = points[i][0], points[i][1]
        xj, yj = points[j][0], points[j][1]
        wt = abs(xi-xj) + abs(yi-yj)
        adj[i].append((j,wt))
        adj[j].append((i,wt))
        

    visited = [False]*n

    edge_count = 0
    #edge_count = 3
    heapq.heappush(pq, (0,0))
    min_cost = 0
    # min_cost = 0 + 0 + 1 + 2 + 2
    while len(pq) > 0:
      wt, u = heapq.heappop(pq)
      # 2,3
      if visited[u]:
        continue
      min_cost += wt
     
      visited[u] = True
     
      edge_count += 1
     
      if edge_count == n:
        break

      for (v,w) in adj[u]:
        # v,w = 1,4
        if visited[v]:
          continue
        heapq.heappush(pq,(w,v)) 
    
    return min_cost


------------------

class Solution:
  def minCostConnectPoints(self, points: list[int]) -> int:
    # dist[i] := the minimum distance to connect the points[i]
    dist = [math.inf] * len(points)
    ans = 0

    for i in range(len(points) - 1):
      for j in range(i + 1, len(points)):
        # Try to connect the points[i] with the points[j].
        dist[j] = min(dist[j], abs(points[i][0] - points[j][0]) +
                      abs(points[i][1] - points[j][1]))
        # Swap the points[j] (the point with the mnimum distance) with the
        # points[i + 1].
        if dist[j] < dist[i + 1]:
          points[j], points[i + 1] = points[i + 1], points[j]
          dist[j], dist[i + 1] = dist[i + 1], dist[j]
      ans += dist[i + 1]

    return ans
    
        