"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "ababc", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

input s : 'aaaa' p : 'aa'
output : [0,1,2]

1. create a xor of all char in p.
2. find 

"""
class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    res = []
    m,n = len(s), len(p)

    if n > m:
      return []
    p_chars = dict()
    for c in p:
      p_chars[c] = 1 + p_chars.get(c,0)
    s_chars = dict()
    
    for idx in range(n):
      s_chars[s[idx]] = 1 + s_chars.get(s[idx],0)

    if p_chars == s_chars:
      res.append(0)

    for idx in range(n, m, 1):
      s_chars[s[idx-n]] -= 1
      if s_chars[s[idx-n]] == 0:
        del s_chars[s[idx-n]]
      s_chars[s[idx]] = 1 + s_chars.get(s[idx],0) 
      if p_chars == s_chars:
        res.append(idx-n+1)
    

    return res   
      

