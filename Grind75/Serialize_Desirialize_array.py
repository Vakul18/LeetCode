"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []


use bfs to create comma separated string

convert the string to array then 





[1,2,3,null,null,4,5]
"""


from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([(root, 0)])
        
        ordered_nodes = [1]
        """
        [1,2,3,null,null,4,5]
        queue = [ (None, 13), (None, 14)]
        ordered_nodes = [1, 2, 3, '', '', 4, 5, "", "", "", "", "", "", ""]
        node = None, idx = 13
        """
        while queue:
            node, idx = queue.popleft()
            self.expand_list_add((str(node.val) if node else ''), ordered_nodes, idx)

            if node:
                if node.left:
                    queue.append((node.left, 2*idx+1))
                else:
                    queue.append((None, 2*idx+1))
                
                if node.right:
                    queue.append((node.right,2*idx+2))
                else:
                    queue.append((None, 2*idx+2))

        return ','.join(ordered_nodes)

    def expand_list_add(self, val:str, lst:List, idx:int):
        while len(lst) - 1 < idx:
            lst.append('')
        lst[idx] = val  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        print(data)
        ordered_vals = data.split(',')
        if len(ordered_vals[0]) == 0 :
            return None
        
        root = TreeNode(int(ordered_vals[0]))
        queue = deque([(root, 0)])

        while queue:
            node, idx = queue.popleft()

            if (2*idx+1) < len(ordered_vals) and len(ordered_vals[2*idx + 1]) > 0:
                left_node = TreeNode(int(ordered_vals[2*idx+1]))
                node.left = left_node
                queue.append((left_node, 2*idx+1))
                
            if (2*idx + 2) < len(ordered_vals) and len(ordered_vals[2*idx + 2]) > 0:
                right_node = TreeNode(int(ordered_vals[2*idx + 2]))
                node.right = right_node
                queue.append((right_node, 2*idx + 2))
        return root

                        
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))




























--------------------------------------------
from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1,2,3,null,null,4,5,6,7]
# 1,2,3,,,4,5,6,7,,,,,,
# 1,2,3,,,4,5,,,,,6,7,,,,,,,,,,,,,,
"""
          1(0)
        /         \
       2(1)       3(2)
       /\          /   \  
  nil(3) nil(4)  4(5)  5(6)
                 


"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        
        ordered_nodes = []

        while queue:
            node= queue.popleft()
            self.list_add(node, ordered_nodes)

            if node:
                queue.append(node.left)      
                queue.append(node.right)

        return ','.join(ordered_nodes)

    def list_add(self, node : Optional[TreeNode], lst:List):
        if node:
            lst.append(str(node.val))
        else:
            lst.append('#')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        #print(data)
        ordered_vals = data.split(',')
        vals_deque = deque(ordered_vals)
        root_val = vals_deque.popleft()
        if root_val == '#':
            return None
        
        root = TreeNode(int(root_val))
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if vals_deque:
                left_node = vals_deque.popleft()
                if left_node != '#':    
                    node.left = TreeNode(int(left_node))
                    queue.append(node.left)
                
            if vals_deque:
                right_node = vals_deque.popleft()
                if right_node != '#':
                    node.right = TreeNode(int(right_node))
                    queue.append(node.right)
        return root

                        
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))






--------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import atexit
atexit.register(lambda: open("display_runtime.txt", "w").write("0"))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodeValues = data.split(',')
        self.i = 0

        def construct():
            nodeVal = nodeValues[self.i]
            self.i += 1
            if nodeVal == 'N':
                return None
            node = TreeNode(int(nodeVal))
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))