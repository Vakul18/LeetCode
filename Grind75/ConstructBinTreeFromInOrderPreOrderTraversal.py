"""
Construct Binary Tree from Preorder and Inorder Traversal
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inMap = dict()
    for idx, val in enumerate(inorder):
      inMap[val] = idx       

    def helper(inMap, inSIdx, inEIdx, preSIdx, preEIdx):
      if preSIdx > preEIdx:
        return None
      node = TreeNode(preorder[preSIdx])
      inRoot = inMap[node.val]
      leftNums = inRoot -  inSIdx
      node.left = helper(inMap, inSIdx, inRoot-1,  preSIdx + 1,  preSIdx + leftNums)
      node.right = helper(inMap, inRoot+1, inEIdx, preSIdx + leftNums + 1, preEIdx)
     
      return node

    return helper(inMap, 0, len(inorder)-1, 0, len(preorder)-1)



     