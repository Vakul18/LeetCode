"""
Duplicate Subtree

Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.

Note: Two same leaf nodes are not considered as subtree as size of a leaf node is one. 
"""
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
  def dupSub(self, root):
    nodes_set = set()
    found = False
    def search_dup(node):
      nonlocal found
      if not node:
        return '#'

      left = search_dup(node.left)
      right = search_dup(node.right)
      
      encoding = f'{node.data};{left};{right}'

      if (node.left or node.right) and encoding in nodes_set:
        found = True
      
      nodes_set.add(encoding)
      return encoding
    
    search_dup(root)
    return 1 if found  else 0