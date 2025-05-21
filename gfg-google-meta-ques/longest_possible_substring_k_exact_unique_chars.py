"""
Longest Substring with K Uniques
Difficulty: MediumAccuracy: 34.65%Submissions: 188K+Points: 4
Given a string s, you need to print the size of the longest possible substring with exactly k unique characters. If no possible substring exists, print -1.

"""
#User function Template for python3

class Solution:
  def longestKSubstr(self, s, k):
    n = len(s)
    if n < k:
      return -1
    
    char_map = dict()
    max_size = -1
    l = 0
    curr_size = 0
    for i in range(n):
      c = s[i]
      if c in char_map:
        char_map[c] += 1
      else:
        char_map[c] = 1

      
      while len(char_map) > k:
        c_l = s[l]
        char_map[c_l] -= 1
        if char_map[c_l] == 0:
          del char_map[c_l]
        l += 1
      if len(char_map) == k:
        max_size = max(max_size, i-l+1)
      
      
    return max_size
    