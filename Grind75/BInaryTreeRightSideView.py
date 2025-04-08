"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

   1
  /  \
 2    4
6 3  7 8
   9

1. store all the elements in a level as list in quwuw
2. during each deque operation on queue output the last elemetn in the list.
3. repeat till queue is empty
"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    queue = deque([[root]])
    right_side = []
    while queue:
      level = queue.popleft()
      right_side.append(level[-1].val)
      new_level = []
      for node in level:
        if node.left:
          new_level.append(node.left)
        if node.right:
          new_level.append(node.right)
      if len(new_level) > 0:
        queue.append(new_level)

    return right_side

--------------------------------------------

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    prev_level = [root]
    right_side = []
    while len(prev_level)>0:
      right_side.append(prev_level[-1].val)
      new_level = []
      for node in prev_level:
        if node.left:
          new_level.append(node.left)
        if node.right:
          new_level.append(node.right)
      
      prev_level = new_level


    return right_side


-----------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        queue = deque([root])
        view = []

        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if i == 0:
                    view.append(node.val)
                if node.right:
                    queue.append(node.right)               
                if node.left:
                    queue.append(node.left)
                

        return view

        
        return view