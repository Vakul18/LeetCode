"""
k-th Smallest in BST
Difficulty: MediumAccuracy: 43.53%Submissions: 141K+Points: 4Average Time: 40m
Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1.

Examples:

Input: root = [2, 1, 3], k = 2
    
Output: 2
Explanation: 2 is the 2nd smallest element in the BST.
Input: root = [2, 1, 3], k = 5
    
Output: -1
Explanation: There is no 5th smallest element in the BST as the size of BST is 3.
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3
     
Output: 10
Explanation: 10 is the 3rd smallest element in the BST.
Constraints:

1 <= number of nodes, k <= 105
1 <= node->data <= 105
"""
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
 2
1 3
   4
'''

class Solution: 
  def kthSmallest(self, root, k):
    nums = []
    def inorder(node):
      if not node:
        return
      inorder(node.left)
      nums.append(node.data)
      if len(nums) == k:
        return
      inorder(node.right)
      return
    inorder(root)
    return nums[k-1] if len(nums) >= k else  -1


#####################
class Solution: 
  def kthSmallest(self, root, k):
    curr = root
    inorder = []
    k_node = None
    while curr:
      if not curr.left:
        inorder.append(curr.data)
        if len(inorder) == k:
          k_node = curr
          break
        curr = curr.right
      else:
        prev = curr.left
        while prev.right and prev.right != curr:
          prev = prev.right
 
        if prev.right == curr:
          prev.right = None
          inorder.append(curr.data)
          if len(inorder) == k:
            k_node = curr
            break
          curr = curr.right
        else:
          prev.right = curr
          curr = curr.left

    return k_node.data if k_node else -1






      

    
