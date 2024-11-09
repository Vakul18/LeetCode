"""
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language. If no valid ordering of letters is possible, then return "".
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Input:  n = 5, k = 4, dict = {"baa","abcd","abca","cab","cad"}
Output: 1
Explanation: Here order of characters is 'b', 'd', 'a', 'c' Note that words are sorted and in the given language "baa" comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

1st char b->a->c
3rd char b->d
4th char d->a


"""

from typing import List
from collections import deque

class Solution:
  	def findOrder(self, dict1: List[str], n: int, k: int) -> str:
		idx = 0
		adj = {chr(i + 97):[] for i in range(k)}
		indeg = dict()

		for i in range(1,n):
			firstWord = dict1[i-1]
			secondWord = dict1[i]
			
			for j in range(min(len(firstWord), len(secondWord))):
			    if firstWord[j] != secondWord[j]:
			        adj[firstWord[j]].append(secondWord[j])
			        if firstWord[j] not in indeg:
			            indeg[firstWord[j]] = 0
			        if secondWord[j] in indeg:
			            indeg[secondWord[j]] += 1
			        else:
			            indeg[secondWord[j]] = 1
			        break;
			
	
				
			
        print(adj)
        print(indeg)
		q = deque()
        #print('11')
		for key,value in indeg.items():
			if value == 0:
				q.append(key)
		#print('12')
		
		ordering = []
		while q:
			u = q.popleft()
			ordering.append(u)
			if u not in adj:
                continue
			#print('1')
			for v in adj[u]:
				indeg[v] -= 1
				if indeg[v] == 0:
					q.append(v)

			#print('2')

        
        #print(ordering)
		return ordering


############## Using DFS

from typing import List
from collections import deque

class Solution:
  	def findOrder(self, dict1: List[str], n: int, k: int) -> str:
		idx = 0
		adj = {chr(i + 97):[] for i in range(k)}
		indeg = dict()

		for i in range(1,n):
			firstWord = dict1[i-1]
			secondWord = dict1[i]
			
			for j in range(min(len(firstWord), len(secondWord))):
			    if firstWord[j] != secondWord[j]:
			        adj[firstWord[j]].append(secondWord[j])
			        if firstWord[j] not in indeg:
			            indeg[firstWord[j]] = 0
			        if secondWord[j] in indeg:
			            indeg[secondWord[j]] += 1
			        else:
			            indeg[secondWord[j]] = 1
			        break;
			
	
				
			
        ordering = []
        visited = set()
        
        def dfs(u):
            if u in visited:
                return
            visited.add(u)
            for v in adj[u]:
                dfs(v)
                
            ordering.append(u)
            
        for u in adj:
            dfs(u)
            
        ordering.reverse()

			#print('2')

        
        #print(ordering)
		return ordering
			