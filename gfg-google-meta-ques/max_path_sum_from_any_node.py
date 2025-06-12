"""
Maximum path sum from any node

Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.
"""
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
  def findMaxSum(self, root):
    max_sum = float('-inf')
    def max_path(node):
      nonlocal max_sum
      if not node:
        return 0

      left_sum = max_path(node.left)
      right_sum = max_path(node.right)
      
      max_sum = max(max_sum, node.data + left_sum, node.data + right_sum, node.data + left_sum + right_sum, node.data)
      return max(node.data + left_sum, node.data + right_sum, node.data)

    max_path(root)
    return max_sum
     
    