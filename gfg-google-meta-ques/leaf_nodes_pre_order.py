"""
Given a preorder traversal of a BST, find the leaf nodes of the tree without building the tree.


Examples:

Input: preorder[] = [5, 2, 10]
Output: [2, 10]
Explaination: 

2 and 10 are the leaf nodes as shown in the figure.
Input: preorder[] = [4, 2, 1, 3, 6, 5]
Output: [1, 3, 5]
Explaination: 

1, 3 and 5 are the leaf nodes as shown in the figure.
Input: preorder[] = [8, 2, 5, 10, 12]
Output: [5, 12]
Explaination: 

5 and 12 are the leaf nodes as shown in the figure.

     5
   /   \
   2     6
  /\      \
  1 3      8
 / 
-1
pre = [5, 2, 1, -1, 3, 6, 8]

- 1st element is root
- last element is always leaf
- find the last decreasing element before increasing element found.

5 2 10

[5 2]


9 1 8 4 2 3 7 10 11
  |
st = [9, 8]
leaves = 1 

1 2 3 4 7 8 9 10 11
|


   9
  / \
 1   10  
  \    \
   8    11
  /
 4
/ \	
2  7
 \
  3


"""
class Solution:
  def leafNodes(self, preorder):
    leaves = []
    idx = 0
    n = len(preorder)
    st = []
    for idx in range(n-1):
      found = False
      
      if preorder[idx] > preorder[idx+1]:
        st.append(preorder[idx])
      else:
        while st and preorder[idx+1] > st[-1]:
          st.pop()
          found = True
      if found:
        leaves.append(preorder[idx])
    
     
    leaves.append(preorder[-1])
    return leaves


#################
class Solution:
  def leafNodes(self, preorder):
    leaves = []
    inorder = sorted(preorder)

    inorder_map = dict()
    for idx, num in enumerate(inorder):
      inorder_map[num] = idx

    ind = [0]
    n = len(preorder)
  
    def binarySearch(num, l, r):
      m = (l + r)//2
    
      if inorder[m] == num:
        return m

      if inorder[m] > num:
        return binarySearch(num, l, m-1)
      else:
        return binarySearch(num, m+1, r)
   
    def search(l, r, n):
      if l == r:
        leaves.append(preorder[ind[0]])
        ind[0] += 1
        return

      if l > r or l >= n or r < 0:
        return

      num = preorder[ind[0]]
      loc = inorder_map[num]
    
      ind[0] += 1
      search(l, loc-1, n)
      search(loc+1, r, n)
        
    
    search(0, n-1, n)
    return leaves
