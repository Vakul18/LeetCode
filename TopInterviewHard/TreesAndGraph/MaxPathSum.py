# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

    -2
  -1   -3
3    4

  2
1   3

2


 1
2 3

  2
-1

(2)
 leftsum = (-1)
		left = 0
   		right = 0
		return -1
rightsum = 0



"""
class Solution:
	def __init__(self):
		self.maxPath = float('-inf')	

	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		self.GetMaxPath(root)
		return self.maxPath
	
	def GetMaxPath(self, node):
		if not node:
			return 0
		
		leftPathSum = self.GetMaxPath(node.left)
		rightPathSum = self.GetMaxPath(node.right)
		print(leftPathSum + node.val + rightPathSum)
		
		currentPathValue = max(leftPathSum + node.val, rightPathSum + node.val, node.val, leftPathSum + node.val + rightPathSum)
		if currentPathValue > self.maxPath:
			self.maxPath = currentPathValue

		return max(leftPathSum + node.val, rightPathSum + node.val, node.val)

	