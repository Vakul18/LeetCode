"""
Minimum repeat to make substring

Given two strings s1 and s2. Return a minimum number of times s1 has to be repeated such that s2 is a substring of it. If s2 can never be a substring then return -1.

Note: Both the strings contain only lowercase letters.

Examples:

Input: s1 = "ww", s2 = "www"
Output: 2
Explanation: Repeating s1 two times "wwww", s2 is a substring of it.
Input: s1 = "abcd", s2 = "cdabcdab" 
Output: 3 
Explanation: Repeating s1 three times "abcdabcdabcd", s2 is a substring of it. s2 is not a substring of s1 when it is repeated less than 3 times.
Input: s1 = "ab", s2 = "cab"
Output: -1
Explanation: No matter how many times we repeat s1, we can't get a string such that s2 is a substring of it.

"abcxy" "ajbjcjxjy"
-1

"cab" "abc"
1
"abc""abc"

"cababca" "abc"
abc|abc|a


"caxabc" "cab" 
 |          |


abcd
cdabcdab 

abcd|abcd|abcd

wwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

aabaa
aaab

aabaa|aabaa
"""
class Solution:
  def minRepeats(self, s1, s2):
    s1_i = 0
    repeats = 1

    while s1_i < len(s1):

      j, k repeats = s1_i, 0, 1
      while j < len(s1) and k < len(s2) and s1[j] == s2[k]:
        j += 1
        k += 1
        if j == len(s1) and k < len(s2):
          j = 0
          repeats += 1

      if k == len(s2):
        return repeats

      s1_i += 1   
   
    return -1


###########################################

"""
aabaa
aaab

lps = [0, 1, 2, 0]
"""
import math
class Solution:
  def minRepeats(self, txt, pat):
    m , n = len(pat), len(txt)
    lps = [0] * m

    def compute_lps(m):
    
      pre_idx , suff_idx = 0, 1

      while suff_idx < m:
        if pat[pre_idx] == pat[suff_idx]:
          pre_idx += 1
          lps[suff_idx] = pre_idx
          suff_idx += 1
        else:
          if pre_idx == 0:
            lps[suff_idx] = 0
            suff_idx += 1
          else:
            pre_idx = lps[pre_idx-1]
    
    compute_lps(m)
    i, j = 0 , 0
    repeat = 1
    max_repeat = max(math.ceil(m/n) + 1, 2)
    while repeat <= max_repeat and i < n:
      if pat[j] == txt[i]:
        i += 1
        j += 1
        if j == m:
          return repeat
        elif i == n:
          i = 0
          repeat += 1
      else:
        if j == 0:
          i += 1
        else:
          j = lps[j-1]

    return -1
 