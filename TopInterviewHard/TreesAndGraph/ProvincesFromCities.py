"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

[
 [1,1,0],
 [1,1,0],
 [0,0,1]
]

0-1
2
"""
from collections import deque

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n = len(isConnected)
		stack = deque()
		processed = [False] * n
		provinceCount = 0
		for i in range(0,n):
			if processed[i]:
				continue
			stack.append(i)
			processed[i] = True
			#print(processed)
			#print(f'index : {i}')
			provinceCount += 1
			#print(f'province count {provinceCount}')
			while(stack):
				city = stack.pop()
				neighbours = []
				for otherCity in range(0, n):
					if otherCity == city or processed[otherCity] or (not isConnected[city][otherCity]):
						continue
					stack.append(otherCity)
					processed[otherCity] = True

		return provinceCount
	

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        neighbors = {}
        for i in range(n):
            if i not in neighbors:
                neighbors[i] = []
            for j in range(n):
                if isConnected[i][j] == 1:
                    neighbors[i].append(j)

        V = set()
        for i in range(n):
            V.add(i)

        stack = []
        count = 0

        while V:
            source = V.pop()
            stack.append(source)
            count += 1

            while stack:
                cur = stack.pop()    
                for vertex in neighbors[cur]:
                    if vertex in V:
                        V.remove(vertex)
                        stack.append(vertex)
        
        return count
	
	
	