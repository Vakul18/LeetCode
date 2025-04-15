"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    counter = [0]
    smallest = [float('-inf')]
    def helper(node):
      if not node or counter[0] >= k:
        return

      helper(node.left)

      counter[0] += 1
      if counter[0] == k:
        smallest[0] = node.val

      helper(node.right)
    helper(root)
    return smallest[0]
     