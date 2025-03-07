"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
max = 4
root(1)
	left = 2, right = 1 
		
			
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		max_diameter = 0
		def depth(node):
			nonlocal max_diameter
			if not node:
				return -1
			left_depth = 1 + depth(node.left)
			right_depth = 1 + depth(node.right)
			
			max_diameter = max(max_diameter, left_depth + right_depth + 1)

			return max(left_depth, right_depth)

		
		depth(root)
		return max_diameter - 1
				


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def max_to_leaf(node):
            if node:
                l = max_to_leaf(node.left)
                r = max_to_leaf(node.right)

                nonlocal result
                result = max(result, l + r)

                return 1 + max(l, r)
            return 0

        max_to_leaf(root)
        return result
		