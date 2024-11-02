# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	
		pPath = self.getPath(root, p)
		qPath = self.getPath(root, q)
		#print(self.ppath(pPath))
		#print(self.ppath(qPath))
		idx = 0

		while idx < len(pPath) and idx < len(qPath):
			if not (pPath[idx] == qPath[idx]):
				break
			idx += 1
				
		

		return pPath[idx-1]

	def getPath(self, root, p):
		stack = deque()
		stack.append((root, []))
		nodeFound = False
		if root == p:
			return [root]
		while(stack):
			(node, path) = stack.pop()
			if node.left == p :
				nodeFound = True
				return path + [node] + [node.left]

			if node.right == p :
				nodeFound = True
				return path + [node] + [node.right]
			
			
			newPath = path + [node]

			if node.left:	
				#print(f'Add {node.left.val} with path {self.ppath(newPath)}')
				stack.append((node.left, newPath))
	
			if node.right:	
				#print(f'Add {node.right.val} with path {self.ppath(newPath)}')
				stack.append((node.right, newPath))	

		return []

	#def ppath(self, l):
		#return "-".join([str(li.val) for li in l])
	


	
		
	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root
            elif left:
                return left
            else:
                return right
        return dfs(root, p, q)		


	

	
