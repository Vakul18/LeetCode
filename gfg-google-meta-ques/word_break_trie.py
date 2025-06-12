"""
Word Break (Trie)

Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words. 


Example 1:

Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung",
"mobile","ice","cream", "icecream", "man",
"go", "mango" }, A = "ilike"
Output: 1
Explanation: The string can be segmented as
"i like".
Example 2:

Input: 
n = 12 
B = { "i", "like", "sam", "sung", "samsung",
"mobile","ice","cream", "icecream", "man", 
"go", "mango" }, A = "ilikesamsung" 
Output: 1
Explanation: The string can be segmented as 
"i like samsung" or "i like sam sung".

Your Task:
Complete wordBreak() function which takes a string and list of strings as a parameter and returns 1 if it is possible to break words, else return 0. You don't need to read any input or print any output, it is done by driver code.


Expected time complexity: O(n*l+|A|2) where l is the leght of longest string present in the dictionary and |A| is the length of string A
Expected auxiliary space: O(|A| + k) , where k = sum of length of all strings present in B

 

Constraints:
1 <= N <= 12
1 <= s <=1000 , where s = length of string A
 The length of each word is less than 15.
"""
## Time complexity : O(l*n^2)
## Space complexity : O(m + n)
#User function Template for python3

class Solution:
  def wordBreak(self, A, B):
    n = len(A)
    dp = [False] * (n+1)
    dp[0] = True
    dict = set(B)
     
    for i in range(n):
      for j in range(i+1):
        word = A[j:i+1]
        if word in dict:
          dp[i+1] = dp[j]
          if dp[i+1]:
            break

    return dp[n]

################################
class TNode:
  def __init__(self):
    self.children = dict()
    self.eow = False

class Solution:
  def wordBreak(self, A, B):
    n = len(A)
    root = TNode()

    for word in B:
      curr_node = root
      for char in word:
        if char not in curr_node.children:
          curr_node.children[char] = TNode()
        curr_node = curr_node.children[char]
      curr_node.eow = True

    dp = [False] * (n+1)
    dp[n] = True

    for i in range(n-1, -1, -1):
      curr_node = root
      for j in range(i, n):
        if A[j] in curr_node.children:
          curr_node = curr_node.children[A[j]]
          
          if curr_node.eow and dp[j+1]:
            dp[i] = True
            break
        else:
          break

    return dp[0]
    



    
    
