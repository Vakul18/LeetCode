"""
Connect Nodes of Levels
Difficulty: MediumAccuracy: 55.78%Submissions: 101K+Points: 4Average Time: 45m
Given a binary tree, connect the nodes that are at the same level. You'll be given an addition nextRight pointer for the same.

Initially, all the next night pointers point to garbage values. Your function should set these pointers to the point next right for each node.
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>     3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2          4 --> 1 -----> 2 -------> NULL

 

Examples:

Input:
     3
   /  \
  1    2
Output:
[3, 1, 2]
[1, 3, 2]
Explanation:The connected tree is
        3 ------> NULL
     /    \
    1-----> 2 ------ NULL
Input:
      10
    /   \
   20   30
  /  \
 40  60
Output:
[10, 20, 30, 40, 60]
[40, 20, 60, 10, 30]
Explanation:The connected tree is
         10 ----------> NULL
       /     \
     20 ------> 30 -------> NULL
  /    \
 40 ----> 60 ----------> NULL
Input:
       15
     /  \
    10   20
   / \   / \
  8   12 18 25

Output:
[15, 10, 20, 8, 12, 18, 25]
[8, 10, 12, 15, 18, 20, 25]
Explanation:The connected tree is
         15 ----------> NULL
       /    \
     10 ------> 20 --------> NULL
    /  \        /  \
   8 --> 12 -->18 --> 25 --> NULL

root

queue - [15, 10, 20]
 
"""
from collections import deque
import sys

# Tree Node
class Node:
  def __init__(self, val):
    self.right = None
    self.data = val
    self.left = None
    self.nextRight = None

class Solution:
  def connect(self, root):
    queue = deque([root])

    while queue:
      prev_node = queue.popleft()
      level = []
      if prev_node.left:
        level.append(prev_node.left)
      if prev_node.right:
        level.append(prev_node.right)

      while queue:
        node = queue.popleft()
        prev_node.nextRight = node
        if node.left:
          level.append(node.left)
        if node.right:
          level.append(node.right)
        prev_node = node

      for node in level:
        queue.append(node)

    return root
      
      












        