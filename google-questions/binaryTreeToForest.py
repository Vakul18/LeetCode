"""
left child: 2i + 1
right child: 2i + 2

[1,2,3] becomes the tree                                                                                                                                                                                           
      1                                                                                                                                                                                                            
    2   3                                                                                                                                                                                                          
                                                                                                                                                                                                                   
[1,null,3] becomes a tree without a left child.                                                                                                                                                                    
     1                                                                                                                                                                                                             
       3

Example 1:                                                                                                                                                                                                         
Input: tree = [1,2,3], to_delete = [1]                                                                                                                                                                             
Output: [ [2], [3] ]                                                                                                                                                                                               
                                                                                                                                                                                                                   
Example 2:                                                                                                                                                                                                         
Input: tree = [1,2,3,4], to_delete = [4]                                                                                                                                                                           
Output: [ [1, 2, 3] ]                                                                                                                                                                                              
                                                                                                                                                                                                                   
Example 3:                                                                                                                                                                                                         
Input: tree = [1,2,3,4,5,6,7], to_delete = [3,5]                                                                                                                                                                   
Output: [ [1, 2, null, 4], [6], [7]] 

Example 4:                                                                                                                                                                                                         
Input: tree = [1,2,3,4, null,6,7,8], to_delete = [3,6]                                                                                                                                                                   
Output: [ [1, 2, null, 4, null, null, 8], [6], [7]] 

   1
 2    3
4 5  6 7

Example 4:                                                                                                                                                                                                         
Input: tree = [1,2,3,4, null,6,7,8], to_delete = [4,1]                                                                                                                                                                   
Output: [[2], [8], [3,6,7]]

    1
  2    3
 4    6 7
8

[ [2], [3,6,7], [8]]

linear search- search keys
[6,3]



"""
from typing import List
from collections import deque



class Tree:
    def __init__(self, tree: List):
        self.tree = tree

    def getLeftChildIdx(self, idx):
        return idx * 2 + 1

    def getRightChildIdx(self, idx):
        return idx * 2 + 2

    def remove(self, keys: List):
        keys_set = set(keys)

        n = len(self.tree)
        keys_idxs = []

        for idx in range(n - 1, -1, -1):
            if self.tree[idx] in keys_set:
                keys_idxs.append(idx)

        forest = []

        for key_idx in keys_idxs:
            self.tree[key_idx] = None
            leftSubTree = self.extractSubTree(self.getLeftChildIdx(key_idx))
            if leftSubTree:
                forest.append(leftSubTree)

            rightSubTree = self.extractSubTree(self.getRightChildIdx(key_idx))
            if rightSubTree:
                forest.append(rightSubTree)

        leftOverMainTree = []
        nonEmptyIdxFound = False
        for idx in range(n - 1, -1, -1):
            if nonEmptyIdxFound:
                leftOverMainTree.append(self.tree[idx])
            elif self.tree[idx]:
                nonEmptyIdxFound = True
                leftOverMainTree.append(self.tree[idx])

        if len(leftOverMainTree) > 0:
            forest.append(leftOverMainTree[::-1])

        return forest

    def extractSubTree(self, idx):
        max_idx = len(self.tree) - 1
        if idx > max_idx:
            return []

        tree = []

        queue = deque([idx])
        while queue:
            node = queue.popleft()
            if node <= max_idx:
                tree.append(self.tree[node])
                self.tree[node] = None

            children = [2 * node + 1, 2 * node + 2]

            for child in children:
                if child <= max_idx:
                    queue.append(child)

        for idx in range(len(tree) - 1, -1, -1):
            if tree[idx] is not None:
                break
            tree.pop()

        return tree
		
		

arr = [1,2,3,4, None,6,7,8]
del_keys = [1,4]



tree = Tree(arr)
result = tree.remove(del_keys)
print(result)			

		



"""
  Can the original tree have None in it? (That is, can it be non-complete?)
  - Assume yes.

  If nodes_to_remove is empty, how should we react? Raise an exception, or return
  the list unmodified?
  - Assume return unmodified.

  Can we assume the original tree is valid? If not, should we validate the entire
  structure, or just raise an exception when we encounter it?
  - If there are multiple trees in the array, just ignore the others.


  We can write a function to visit the nodes in the tree using BFS.  In that,
  we can test whether a node is equal and add its index to a list.  Later,
  we go through the list and mark those nodes as None.  Then, we can visit the
  nodes again, and maintain a set of visited nodes.  We can then continually
  visit the first unvisited index.

  The main difficulty would be in efficiently determining the next node. If we
  just have a list of booleans initialized to False (for unvisited), then we
  could have to do a O(N) traversal for every pass.  Making it WCS O(N^2)  We
  could speed that up, I suppose, by maintaining a left pointer to the lowest
  visited last time.  Then we're basically doing the visit operation twice
  (and overall, it should be O(N).)
  """
  from collections import deque
  from typing import (
      Callable,
      List,
      Optional,
      TypeVar,
  )

  T = TypeVar("T")


  def visit(
      tree: List[Optional[T]],
      visitor: Callable[[int, Optional[T]], None],
      root: int = 0,
  ):
      """Visit each node of the tree rooted at the given index using BFS."""
      q = deque([root])
      while q:
	  index = q.pop()
	  visitor(index, tree[index])
	  children = [index * 2 + 1, index * 2 + 2]
	  for child in children:
	      if child < len(tree) and tree[child] is not None:
		  q.appendleft(child)


  class _RootFinder:
      """Finds the next root to visit when traversing a forest."""

      def __init__(self, tree):
	  # Invariant: everything to the left of min_visited has been visited.
	  # After calling find_next_root, min_visited will either point to an
	  # unvisited node, or the end of the tree.
	  self.min_visited = 0
	  self.visited = [False] * len(tree)
	  # We need the tree so that we can skip over null values (empty branches/leaves.)
	  self.tree = tree

      def find_next_root(self) -> Optional[int]:
	  """Get the root of the next tree to visit in the forest, if any."""
	  if self.min_visited >= len(self.visited):
	      return None
	  while self.min_visited < len(self.visited):
	      if self.tree[self.min_visited] is None:
		  self.visited[self.min_visited] = True
	      if not self.visited[self.min_visited]:
		  return self.min_visited
	      self.min_visited += 1
	  return None

      def mark_visited(self, index):
	  self.visited[index] = True


  def remove_nodes(
      tree: List[Optional[T]],
      nodes_to_remove: List[T],
  ) -> List[List[Optional[T]]]:
      """Remove nodes from the given tree.

      WARNING: Modifies input tree.

      Args:
	  tree: A list-based representation of an array. We assume there is only a
	      single, valid tree in the array.  We ignore any unconnected components.
	  nodes_to_remove: A list of the values to remove from the tree.

      Returns:
	  A list of trees formed by removing the nodes. (If a removing a node orphans
	  that subtree, it becomes a new tree.)
      """
      if len(tree) == 0:
	  return []

      # First, we mark the indices to delete. We do this to avoid modifying while
      # traversing. It would be safe to do that now, but this will make it easier to
      # support things such as parallelism in the future.
      indices_to_delete = []  # type: List[int]
      # Remove duplicates
      to_delete = set(nodes_to_remove)

      def mark_indices_to_remove(index, node):
	  if node in to_delete:
	      indices_to_delete.append(index)
      visit(tree, mark_indices_to_remove)
      for index in indices_to_delete:
	  tree[index] = None

      # Continually traverse trees at the given roots.  By using _RootFinder, we
      # can iterate through the trees in O(N) time.
      root_finder = _RootFinder(tree)
      trees = []  # type: List[List[Optional[T]]]
      while (root := root_finder.find_next_root()) is not None:
	  curr_tree = []  # type: List[Optional[T]]

	  def do_visit(index, node):
	      root_finder.mark_visited(index)
	      while (index - root) > len(curr_tree):
		  curr_tree.append(None)
	      curr_tree.append(node)

	  visit(tree, do_visit, root)
	  trees.append(curr_tree)

      return trees




