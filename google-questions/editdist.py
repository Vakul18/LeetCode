"""
Given two strings s1 and s2. Return the minimum number of operations required to convert s1 to s2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character

Input: s1 = "geek", s2 = "gesek"
Output: 1

Input: s1 = "geek", s2 = "gesekek"
Output: 3
ge:ge
ek:ek
sek
Input: s1 = "geek", s2 = "geseyek"
                |             | 
1.
g e   e     k
g e s e y e k

2.
""
"a"
3.
""
abc
abc
""

4. 
axy
bcde

5. 
aee
bcde

a-b, a-c, a-d, a-e
x-b, x-c, x-d, x-e
y-b, y-c, y-d, y-e








if string are same len
 count no. of diff chars
else
 q


fsyejylryn
snmq

long_s = fsyejylryn, short_s = snmq
edit_dist = 10
i = 0 , j = 0

"""
class Solution:
    def editDistance(self, s1, s2):
        short_s, long_s = s2 if len(s1) > len(s2) else s1, s1 if len(s1) > len(s2) else s2
        
        edit_dist = len(long_s)
        i = 0
   
        while i < len(short_s):
            j = 0
            while j < len(long_s) and i < len(short_s):
                if short_s[i] == long_s[j]:
                    i += 1
                    edit_dist -= 1
                j += 1
            i += 1
        return edit_dist

"""
fsyejylryn
snmq

mdl
qhszmmbgi

[0 0 0 0]
[0 1 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]

i,j

delete
1 + dp[i-1][j]

insert
1 + dp[i][j-1]

replace
1 + dp[i-1][j-1]

"""

class Solution:
    def editDistance(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[0]*(m+1) for _ in range(0,n+1)]
        
        for i in range(0,n+1):
            dp[i][0] = i

        for j in range(0,m+1):
            dp[0][j] = j
    
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                 if s1[i-1] != s2[j-1]:
                    dp[i][j] = min(1 + dp[i-1][j], 1 + dp[i][j-1], 1 + dp[i-1][j-1])
                 else:
                    dp[i][j] = dp[i-1][j-1]

        return dp[n][m]
            
            
                
            

























