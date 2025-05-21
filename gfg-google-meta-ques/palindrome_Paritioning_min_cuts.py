"""
Given a string s, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.
"""
#User function Template for python3

class Solution:
  def palPartition(self, s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    isPalin = [[False] * n for _ in range(n)]

    for i in range(n):
      isPalin[i][i] = True
    
    for l in range(2, n+1):
      for i in range(n - l + 1):

        j = i + l - 1	

        if len == 2:
          isPalin[i][j] = (s[i] == s[j])
        else:
          isPalin[i][j] = (s[i] == s[j]) and isPalin[i+1][j-1]

        if isPalin[i][j]:
          dp[i][j] = 0
        else:
          dp[i][j] = min([1 + dp[i][k] + dp[k+1][j] for k in range(i,j)])


    return dp[0][n-1]
        


######################



############################################

class Solution:
  def minCut(self, s):
    n = len(s)
    is_palin = [[False] * n for _ in range(n)]
    
    for i in range(n):
      is_palin[i][i] = True
    
    dp = [n] * n

    for l in range(2, n+1):
      for i in range(n-l+1):
        j = i + l - 1
        
        if l == 2:
          is_palin[i][j] = (s[i] == s[j])
        else:
          is_palin[i][j] = (s[i] == s[j]) and is_palin[i+1][j-1]

     
    for i in range(n):
      if is_palin[0][i]:
        dp[i] = 0
      else:
        for j in range(i, 0, -1):
          if is_palin[j][i]:
            dp[i] = min(dp[i], 1 + dp[j-1])

    return dp[n-1]
         

    
 
    