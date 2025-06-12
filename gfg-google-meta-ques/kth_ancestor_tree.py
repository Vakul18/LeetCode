"""
Kth Ancestor in a Tree

Given a binary tree of size  n, a node, and a positive integer k., Your task is to complete the function kthAncestor(), the function should return the kth ancestor of the given node in the binary tree. If there does not exist any such ancestor then return -1.
Note:
1. It is guaranteed that the node exists in the tree.
2. All the nodes of the tree have distinct values.

Examples :

Input: k = 2, node = 4

Output: 1
Explanation:
Since, k is 2 and node is 4, so we first need to locate the node and look k times its ancestors. Here in this Case node 4 has 1 as his 2nd Ancestor aka the root of the tree.
Input: k=1, node=3    

Output: 1
Explanation: k=1 and node=3 ,kth ancestor of node 3 is 1.

  1
 / \
2   3
 
k = 1, 3

"""
def kthAncestor(root,k, node):
  k_node = None
  def search(curr_node):
    nonlocal k_node
    if not curr_node:
      return -1

    if curr_node.data == node:
      return 0

    left_search = search(curr_node.left)
    if left_search >= 0:
      if k == (1 + left_search):
        k_node = curr_node
      return 1 + left_search
   
    right_search = search(curr_node.right)
    if right_search >= 0:
      if k == (1 + right_search):
        k_node = curr_node
      return 1 + right_search

    return -1

    
  search(root)
  return k_node.data if k_node else -1
  