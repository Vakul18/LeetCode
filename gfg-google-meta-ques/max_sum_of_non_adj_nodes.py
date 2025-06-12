"""
Given a binary tree with a value associated with each node. Your task is to select a subset of nodes such that the sum of their values is maximized, with the condition that no two selected nodes are directly connected that is, if a node is included in the subset, neither its parent nor its children can be included.

Examples:

Input: root[] = [11, 1, 2]

Output: 11
Explanation: The maximum sum is obtained by selecting the node 11.

Input: root[] = [1, 2, 3, 4, N, 5, 6]

Output: 16
Explanation: The maximum sum is obtained by selecting the nodes 1, 4, 5, and 6, which are not directly connected to each other. Their total sum is 16.  

space complexity : O(logn)
time complexity : O(n)


"""
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
  def getMaxSum(self, root):

    def findPossibleSum(node):
      if not node:
        return (0, 0)

      

      left_sum_excl, left_sum_incl = findPossibleSum(node.left)

      right_sum_excl, right_sum_incl = findPossibleSum(node.right)

      return (max(left_sum_incl, left_sum_excl) +  max(right_sum_excl, right_sum_incl), node.data + left_sum_excl + right_sum_excl)
      

    return max(findPossibleSum(root))
    