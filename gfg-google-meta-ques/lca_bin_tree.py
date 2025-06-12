"""
Given a Binary Tree with all unique values and two nodes value, n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them are present.

LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.

   a
  / \
 b   d
/ \
c  x
"""
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
  def lca(self,root, n1, n2):
    n = (n1, n2)
    def search(node):
      if node is None:
        return None
      elif node.data == n[0] or node.data == n[1]:
        return node


      left = search(node.left)
      right = search(node.right)

      if left and right:
        return node
      elif left:
        return left
      elif right:
        return right
      return None
 
    return search(root)
    

