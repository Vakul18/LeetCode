"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    queue = deque([(1, root)])
    max_level = 1
    while queue:
      level, node = queue.popleft()
      max_level = max(level, max_level)
      
      if node.left:
        queue.append((level+1, node.left))
      if node.right:
        queue.append((level+1, node.right))

    return max_level

-------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else 1+max(self.maxDepth(root.left),self.maxDepth(root.right) )
