"""
Count BST nodes that lie in a given range

Given a Binary Search Tree (BST) and a range l-h (inclusive), your task is to return the number of nodes in the BST whose value lie in the given range.

Examples :

Input: root[] = [10, 5, 50, 1, N, 40, 100], l = 5, h = 45
         
Output: 3
Explanation: There are three nodes in range [5, 45] =  5, 10 and 40.
Input: root[] = [10, 5, 50, 1, N, 40, 100], l = 10, h = 100
         
Output: 4
Explanation: There are four nodes in range [10, 100] = 10, 40, 50 and 100.
Input: root[] = [1, 2, 3], l = 23, h = 95
         
Output: 0
Explanation: There are no nodes in range [23, 95].
Constraints:
1 <= Number of nodes <= 105
1 <= l <= h < =105

     100
   /     \ 
  30     101
/    \
10    90
 \
  20

85-102

 
"""

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque

class Solution:
  def getCount(self, root, l, h):
    queue = deque([root])
    nodes_count = 0
    while queue:
      node = queue.popleft()
      if node.data >= l and node.data <= h:
        nodes_count += 1
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      elif node.data < l and node.right:
        queue.append(node.right)
      elif node.data > h and node.left:
        queue.append(node.left)
    return nodes_count
      
 
      
      














    
    