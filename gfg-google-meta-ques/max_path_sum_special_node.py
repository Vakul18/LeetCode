"""
Max Path Sum 2 Special Nodes
Difficulty: HardAccuracy: 18.39%Submissions: 195K+Points: 8
Given a binary tree in which each node element contains a number. Find the maximum possible path sum from one special node to another special node.

Note: Here special node is a node that is connected to exactly one different node.

Examples:

Input: root = [3, 4, 5, -10, 4, N, N]
                         
Output: 16
Explanation: Maximum Sum lies between special node 4 and 5. 4 + 4 + 3 + 5 = 16.
Input: root = [-15, 5, 6, -8, 1, 3, 9, 2, -3, 0, 4, -1, 10]


Output:  27
Explanation: The maximum possible sum from one special node to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)
Input: root = [3, 4, 1, -10, 4] 

                         
Output: 12
Explanation: Maximum Sum lies between special node 4 and 5. 4 + 4 + 3 + 1 = 12.
Constraints:
2  ≤  number of nodes  ≤  104
-103  ≤ node->data ≤ 103

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
  def maxPathSum(self, root):
    max_sum = float('-inf')
    def find_max_sum(node):
      nonlocal max_sum
      if not node:
        return 0
      
      if not node.left and not node.right:
        return node.data
      
      if node.left and node.right:
        left_sum = find_max_sum(node.left)
        right_sum = find_max_sum(node.right) 
        max_sum = max(max_sum, node.data + left_sum + right_sum)
        return max(left_sum + node.data, right_sum + node.data)
      elif node.left:
        left_sum = find_max_sum(node.left)
        return left_sum + node.data
      else:
        right_sum = find_max_sum(node.right)
        return right_sum + node.data       
      
    
    sum = find_max_sum(root)
    if (not root.left and root.right) or (root.left and not root.right):
      max_sum = max(sum, max_sum)
    return max_sum

######################


class Solution:
    # Initialize the result with a very small number, assuming no path has been found yet.
    res = -999999999

    def maxPathSumUtil(self, root):
        global res  # Reference the global variable res to track the maximum path sum

        # Base case: If the current node is None, return 0 as there is no contribution to the path sum.
        if root is None:
            return 0

        # If the node is a leaf (no left and right children), return its value.
        if root.left is None and root.right is None:
            return root.data

        # Recursive calls to calculate max path sum for left and right subtrees.
        ls = self.maxPathSumUtil(root.left)
        rs = self.maxPathSumUtil(root.right)

        # If both left and right children are present:
        if root.left and root.right:
            # Update res if the path through root has a higher sum than the current max.
            res = max(res, ls + rs + root.data)
            # Return the maximum of the two child sums plus the current node's value for further calculation.
            return max(ls, rs) + root.data

        # If there is only a right child, return the sum from the right child plus the current node's value.
        if root.left is None:
            return rs + root.data
        else:
            # If there is only a left child, return the sum from the left child plus the current node's value.
            return ls + root.data

    def maxPathSum(self, root):
        global res
        # Reset res for each new computation
        res = -999999999

        # Calculate max path sum through utility function
        h = self.maxPathSumUtil(root)

        # If the root is a single-node path without children, update res to include root value if it's higher
        if root.left is None:
            res = max(res, h)
        if root.right is None:
            res = max(res, h)

        return res  # Return the final maximum path sum.
    