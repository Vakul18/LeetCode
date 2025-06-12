"""
Sorted Linked List to BST
Difficulty: HardAccuracy: 53.24%Submissions: 27K+Points: 8
Given a Singly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Linked List.
Note: There might be nodes with the same value.

Examples:

Input: Linked List: 1->2->3->4->5->6->7

Output: 4 2 1 3 6 5 7
Explanation : The BST formed using elements of the linked list is -
        4
      /   \
     2     6
   /  \   / \
  1   3  5   7  
Hence, preorder traversal of this tree is 4 2 1 3 6 5 7
Input: Linked List : 1->2->3->4
 
Ouput: 3 2 1 4
Explanation: The BST formed using elements of the linked list is -

Hence, the preorder traversal of this tree is 3 2 1 4
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1 ≤ Number of Nodes ≤ 106
1 ≤ Value of each node ≤ 106
"""
#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
  def sortedListToBST(self, head):
    n = 0
    curr_node = head
    while curr_node:
      curr_node = curr_node.next
      n += 1
    
    def build_bst(n : int) -> TNode:
      nonlocal node
      if n <= 0:
        return None

      left_node = build_bst(n//2)

      tree_node = TNode(node.data)

      node = node.next

      right_node = build_bst(n - n//2 - 1)

      tree_node.left = left_node
      tree_node.right = right_node
 
      return tree_node

    node = head
    return build_bst(n)
  