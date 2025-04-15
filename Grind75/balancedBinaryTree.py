"""
Given a binary tree, determine if it is height-balanced.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def helper(node):
      if not node:
        return (True,0)

      state, lheight = helper(node.left)
      if not state:
        return False, float('inf')
      state, rheight = helper(node.right)

      if abs(rheight - lheight) > 1:
        return False, float('inf')
      else:
        return True, 1 + max(lheight, rheight)

    return helper(root)[0]
        