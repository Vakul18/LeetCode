"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

   1
 /  \
 2   3
/\   /\
4 5  6 7 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []
    queue = deque([root])
    result = []
    children = []
    level = []
    while queue:
      node = queue.popleft()
      level.append(node.val)

      if node.left:
        children.append(node.left)
      if node.right:
        children.append(node.right)

      if len(queue) == 0:
        result.append(level)
        level = []
        for child in children:
          queue.append(child)

        children = []

    return result


---------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque, defaultdict

        node_deque = deque([(root, 1)])

        if not root:
            return []
        result_dict = defaultdict(list)
        result = []

        # print(node_deque)

        while node_deque:
            
            node, level = node_deque.popleft()
            result_dict[level].append(node.val)
            # print(node)
            # print('====')

            if node.left:
                node_deque.append((node.left, level + 1))
            if node.right:
                node_deque.append((node.right, level + 1))

        for _, lst in result_dict.items():
            result.append(lst)

        return result


        

        
