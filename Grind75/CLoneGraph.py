"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

bfs with visited
org_queue
clone_queue

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		if node is None:
			return None
		visited = dict()
		clone_start_node = Node(node.val, [])
		org_queue = deque([node])
		visited[node] = clone_start_node
		
		while(org_queue):
			curr_node = org_queue.popleft()
			clone_node = visited[curr_node]
			for neighbour in curr_node.neighbors:
				if neighbour not in visited:
					clone_neighbour = Node(neighbour.val, [])
					org_queue.append(neighbour)
					visited[neighbour] = clone_neighbour
				clone_node.neighbors.append(visited[neighbour])


		return clone_start_node












			