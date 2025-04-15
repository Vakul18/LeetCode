"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.checkTree(root)[0]
  
  def checkTree(self, node):
    if not node.left and  not node.right:
      return (True, node.val, node.val)

    lstate, lmax, lmin = True, float('-inf'), float('inf')
    rstate, rmax, rmin = True, float('-inf'), float('inf')

    if node.left:
      lstate, lmax, lmin = self.checkTree(node.left)
    if lstate and node.right:
      rstate, rmax, rmin = self.checkTree(node.right)

    state = lstate and rstate and (node.val > lmax and node.val < rmin)
    
    return state, max(node.val, lmax, rmax), min(node.val, lmin, rmin)


-------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if(low<root.val<high):
                return helper(root.left, low, root.val) and helper(root.right, root.val, high)
            else:
                return False
        return helper(root, float('-inf'), float('inf'))
        


          
        