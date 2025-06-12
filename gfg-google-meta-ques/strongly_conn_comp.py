from typing import List

class Solution:
    def tarjans(self, V: int, adj: List[List[int]]) -> List[List[int]]:
        idx_counter = 0
        disc = [-1] * V
        low = [-1] * V
        on_stack = [False] * V
        stack = []
        result = []
        
        
        for v in range(V):
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
                    low[u] = min(low[u], low[adj[u][nei_visited-1]])
                
                while nei_visited < len(adj[u]):
                    nei = adj[u][nei_visited]
                    nei_visited += 1
                    if disc[nei] == -1:
                        recurse = True
                        call_stack.append((u, nei_visited, False))
                        call_stack.append((nei, 0, True))
                        break
                    elif on_stack[nei]:
                        low[u] = min(low[u], low[nei])
                        
                if recurse:
                    continue
                if low[u] == disc[u]:
                    scc = []
                    while stack:
                        st_u = stack.pop()
                        scc.append(st_u)
                        on_stack[st_u] = False
                        if st_u == u:
                            break
                    result.append(sorted(scc))
        return sorted(result)
        
################## Recursive Solution ###################

from typing import List

class Solution:
  def tarjans(self, V: int, adj: List[List[int]]) -> List[List[int]]:
    st = []
    on_st = set()
    disc = [-1] * V
    low = [-1] * V
    timer = 0
    result = []

    def sccUtil(u):
      nonlocal timer
      disc[u] = low[u] = timer
      timer += 1
      on_st.add(u)
      st.append(u)

      for v in adj[u]:
        if disc[v] == -1:
          sccUtil(v)
          low[u] = min(low[u], low[v])
        elif v in on_st:
          low[u] = min(low[u], low[v])
      
      if low[u] == disc[u]:
        scc = []
        v = -1
        while st:
          v = st.pop()
          on_st.remove(v)
          scc.append(v)
          if v == u:
            break
          

        result.append(sorted(scc))
        

    for u in range(V):
      if disc[u] != -1:
        continue
      sccUtil(u)
      
    return sorted(result)