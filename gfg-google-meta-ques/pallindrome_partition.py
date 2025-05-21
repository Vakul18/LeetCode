"""
Given a String S, Find all possible Palindromic partitions of the given String.
Example 1:

Input:
S = "geeks"
Output:
g e e k s
g ee k s
Explanation:
All possible palindromic partitions
are printed.
Example 2:

Input:
S = "madam"
Output:
m a d a m
m ada m
madam
"""
#User function Template for python3
# time complexity : O(n.2^n), space complexity : O(n)
class Solution:
  def allPalindromicPerms(self, s):
    path = []
    res = []

    def partition(start):
      if start == len(s):
        res.append(path[:])

      for i in range(start+1, len(s)+1):
        sub = s[start:i]
        if sub == sub[::-1]:
          path.append(sub)
          partition(i)
          path.pop()

    partition(0)
    return res


########################

########finds all palindrom partition strings, but not in proper order.
######## O(n.2^n) time complexity, O(n.2^n)
#User function Template for python3

class Solution:
  def allPalindromicPerms(self, s):
    n = len(s)
    dp = [[] for _ in range(n)]
 
    def findAllPalindromes(m1, m2):
      while m1 >= 0 and m2 < n and s[m1] == s[m2]:
        if m1 > 0:
          for partition in dp[m1-1]:
            dp[m2].append(partition + [s[m1:m2+1]])
        else:
          dp[m2].append([s[m1 : m2+1]])
        m1 -= 1
        m2 += 1
        
    for i in range(n):
      l, r = i, i
      findAllPalindromes(l ,r)
      if i > 0 and s[i] == s[i-1]:
        findAllPalindromes(i-1 ,i) 

    return dp[n-1]





      
 
     