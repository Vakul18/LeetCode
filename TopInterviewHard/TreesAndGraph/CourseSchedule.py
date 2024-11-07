"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


2
[[1,0]]

indeg = [0,1]
adj : 0 :[1]

q : {0}


indeg = [0,0]
q : {1}


"""
from collections import deque

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		adj = dict()
		q = deque()
		indeg = [0] * numCourses

		for pair in prerequisites:
			a = pair[0]
			b = pair[1]
			if b not in adj:
				adj[b] = []
		
			adj[b].append(a)
			indeg[a] += 1

		for course in range(0, numCourses):
			if indeg[course] == 0:
				q.append(course)
		topo = []
		while q:
			course = q.popleft()
			topo.append(course)
			if course not in adj:
				continue
			for depCourse in adj[course]:
				indeg[depCourse] -= 1
				if indeg[depCourse] == 0:
					q.append(depCourse)
		
		if len(topo) == numCourses:
			return True
		return False
		
	
	
	
	


	
				
	
