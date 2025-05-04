"""
N = 4
M = 4
A = [1, 2, 3, 4]
B = [4, 1, 2, 1]

9-10-11-12
        |
        1-2-3-4
        \ /\
         5  6
         |
         7
         |
         8

A = [9, 10, 11, 12, 1, 1, 2, 2, 2, 3, 5, 7]
B = [10, 11, 12, 1, 2, 5, 3, 5, 6, 4, 7, 8]



3 conditions while processing a node for scc

1. node is dfs head
	for all nodes in scc, max path len is (scc len + max(indvidual node start path len))
2. node is not dfs head
	add max len to path[node] for which visited is not true.
3. node is visited
	skip as path starting from the node will be already covered.
	
N = 4
M = 4
A = [1, 2, 3, 4]
B = [4, 1, 2, 1]

adj_list = [1 : 4], [2: 1], [3,2], [4: 1]
path = [0,0,0,0]
disc = [1, -1, -1, 2]
low = [1, -1, -1, 1]
visited = [T, F, F, T]
st = [1, 4]
curr_idx = 2
findmax(1)

  
"""
from typing import List
from collections import defaultdict

# Write any import statements here

def getMaxVisitableWebpages1(N: int, M: int, A: List[int], B: List[int]) -> int:
  path = [0] * (N+1)
  low = [-1] * (N+1)
  disc = [-1] * (N+1) 
  curr_idx = [1]
  visited = [False] * (N+1)
  st = [] 
  adj_list = defaultdict(list)

  def findMaxPath(page: int):
    disc[page] = low[page] = curr_idx[0]
    curr_idx[0] += 1
    visited[page] = True
    st.append(page)
    for linked_page in adj_list[page]:
      if disc[linked_page] == -1:
        findMaxPath(linked_page)
        low[page] = min(low[page], low[linked_page])
      elif visited[linked_page]:
        low[page] = min(low[page], low[linked_page])
      
      if not visited[linked_page]: # if linked page is not part of the same scc
        path[page] = max(path[page], path[linked_page])

    if low[page] == disc[page]: #page is dfs head
      scc_len = 0
      scc_pages = []
      while st:
        scc_page = st.pop()
        visited[scc_page] = False
        scc_pages.append(scc_page)
        scc_len += 1
        if scc_page == page:
          break
      best_scc_path = 0
      for scc_page in scc_pages:
        path[scc_page] += (scc_len)
        best_scc_path = max(best_scc_path, path[scc_page])
      for scc_page in scc_pages:
        path[scc_page] = best_scc_path
        
      
  for i in range(M):
    adj_list[A[i]].append(B[i])
  
  for curr_page in range(1, N+1):
    if disc[curr_page] == -1:
      findMaxPath(curr_page)
  
  return max(path)


def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
  idx_counter = 0
  disc = [-1] * (N+1)
  low = [-1] * (N+1)
  on_stack = [False] * (N+1)
  stack = []
  result = []
  max_path = [0] * (N+1)
  adj = defaultdict(list) 

  for i in range(M):
    adj[A[i]].append(B[i])
        
  for v in range(1, N+1):
    if disc[v] != -1:
      continue
    
    call_stack = [(v, 0, True)]
    while call_stack:
      recurse = False
      u, nei_visited, first_visit = call_stack.pop()
      if first_visit:
        idx_counter += 1
        disc[u] = low[u] = idx_counter
        stack.append(u)
        on_stack[u] = True
      else:
        prev_child = adj[u][nei_visited-1]
        low[u] = min(low[u], low[prev_child])
        if not on_stack[prev_child]:
          max_path[u] = max(max_path[u], max_path[prev_child])
    
      while nei_visited < len(adj[u]):
        nei = adj[u][nei_visited]
        nei_visited += 1
        
        if disc[nei] == -1:
          call_stack.append((u, nei_visited, False))
          call_stack.append((nei, 0, True))
          recurse = True
          break
        elif on_stack[nei]:
          low[u] = min(low[u], low[nei])
        else:
          max_path[u] = max(max_path[u], max_path[nei])
       
      if recurse:
        continue 
       
      if low[u] == disc[u]:
        scc = []
        scc_len = 0
        max_scc_path = 0
        while stack:
          st_u = stack.pop()
          scc.append(st_u)
          scc_len += 1
          on_stack[st_u] = False
          max_scc_path = max(max_scc_path, max_path[st_u])
          if st_u == u:
            break
        for scc_u in scc:
          max_path[scc_u] = scc_len + max_scc_path 

  return max(max_path)

        
          

      



# 🧪 Test Cases
if __name__ == "__main__":
    N = 12
    M = 13
    A = [9, 10, 11, 12, 1, 1, 2, 2, 2, 3, 5, 5, 7]
    B = [10, 11, 12, 1, 2, 5, 3, 5, 6, 4, 7, 1, 8]
   
    print(getMaxVisitableWebpages(N, M, A, B))  # Expected output: 6

  


























  
  
  
