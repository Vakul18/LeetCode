#User function Template for python3

class Solution:
    
    #Function to return a list of lists of integers denoting the members 
    #of strongly connected components in the given graph.
    def tarjans(self, V, adj):
        # code here
        disc = [-1] * V
        low = [-1] * V
        sccs = []
        visited = [False] * V
        st = []
        curr_id = [0]
        def sccUtil(node):
            low[node], disc[node] = curr_id[0], curr_id[0]
            curr_id[0] += 1
            visited[node] = True
            st.append(node)
            for v in adj[node]:
                if disc[v] == -1:
                    sccUtil(v)
                    low[node] = min(low[node], low[v])
                elif visited[v]:
                    low[node] = min(low[node], low[v])
            if low[node] == disc[node]:
                scc = []
                while st:
                    u = st.pop()
                    scc.append(u)
                    visited[u] = False
                    if u == node:
                        break
                sccs.append(sorted(scc))
            
        for i in range(V):
            if disc[i]==-1:
                sccUtil(i)
        
        return sorted(sccs)
         

#{ 
 # Driver Code Starts
#Initial Template for Python 3
from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        ob = Solution()
        
        ptr = ob.tarjans(V, adj)
        
        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j==len(ptr[i])-1:
                    print(ptr[i][j],end="")
                else:
                    print(ptr[i][j],end=" ")
            print(",",end="")
        print()
        print("~")
# } Driver Code Ends



-------------

# Iteration solution

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

