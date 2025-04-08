"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


n = 4
[[1,0],[1,2],[1,3]]
1-0 1-2 1-3


n=6
[[3,0],[3,1],[3,2],[3,4],[5,4]]




  1
 / | \ 
2  3 4
      \
       5
        \
         6

 4            5      1           2
 | \          |     / | \        |
 1  5         4    2  3  4       1
 /\  \       /            |      /\
2  3  6      1            5     3  4
            /|            |         |
           2 3            6         5
                                    |
                                    6


1. Find the longest paths b/w any 2 nodes in the tree.
2. Required roots are center 2 nodes, if path consists of evens no. of nodes.
3. Required roots is center 1 nodes, if path consists of odd no. of nodes.

find deg for node

push nodes with deg as 1 to queue

do while queue size > 2
 node = queue.pop()
 for all the connected nodes which are not already processed
   reduce deg by 1
   push those with deg 1 to queue

return elemens in the queue

[[1,0],[1,2],[1,3]]

adj_mat = {{1,[0,2,3]}, {0,[1]}, {2, [1]}, {3, [1]} }
node_deg = {{1,1}, {0,1}, {2,1}, {3,1}}

queue = [3,1]

node = 

"""
from collections import deque



class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if len(edges) == 0:
      return [n-1]
    adj_mat = dict()
    node_deg = dict()
    queue = deque()
    for edge in edges:
      if edge[0] in adj_mat:
        adj_mat[edge[0]].append(edge[1])
      else:
        adj_mat[edge[0]] = [edge[1]]
      if edge[1] in adj_mat:
        adj_mat[edge[1]].append(edge[0])
      else:
        adj_mat[edge[1]] = [edge[0]]

      if edge[0] in node_deg:
        node_deg[edge[0]] += 1
      else:
        node_deg[edge[0]] = 1

      if edge[1] in node_deg:
        node_deg[edge[1]] += 1
      else:
        node_deg[edge[1]] = 1
    
    for idx in range(n):
      if node_deg[idx] == 1:
        queue.append(idx)
    left_over_nodes = n
    while left_over_nodes > 2:
      queue_size = len(queue)
      left_over_nodes -= queue_size
      
      for _ in range(queue_size):
        node = queue.popleft()

        for adj_node in adj_mat[node]:
          node_deg[adj_node] -= 1
          if node_deg[adj_node] == 1:
            queue.append(adj_node)

    roots = []
    while queue:
      roots.append(queue.popleft())

    return roots

      


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge case
        if n == 1:
            return [0]

        # leaf nodes traversal
        # I believe there can be at most 2 in the final answer
        # probably a proof by contradiction here

        Xor = [0] * n
        deg = [0] * n

        for u,v in edges:
            Xor[u] ^= v
            Xor[v] ^= u
            deg[u] += 1
            deg[v] += 1
        

        layer = [u for u in range(n) if deg[u] == 1]
        prev = 0
        nxt = len(layer)

        while True:

            for i in range(prev, nxt):
                u = layer[i]

                p = Xor[u]

                deg[u] -= 1
                deg[p] -= 1
                Xor[p] ^= u

                if deg[p] == 1:
                    layer.append(p)
            
            if len(layer) == nxt:
                return layer[prev:]
            
            prev, nxt = nxt, len(layer)
            
            #if not LAYER:
            #   return layer
            
            # layer = LAYER   
     





