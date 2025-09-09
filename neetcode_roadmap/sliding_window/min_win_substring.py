"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
from collections import defaultdict
import math
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    m, n = len(s), len(t)
    match = 0
    left = 0
    char_map_win = defaultdict(int)
    char_map_t = defaultdict(int)
    res, res_len = 0, float('inf')
     
    for char in t:
      char_map_t[char] += 1

    need = len(char_map_t.keys())

    for idx, char in enumerate(s):
      if char in char_map_t:
        char_map_win[char] += 1
        if char_map_win[char] == char_map_t[char]:
          match += 1
        
        while match == need:
          if res_len > idx - left + 1:
            res = left
            res_len = idx - left + 1
          if s[left] in char_map_win:
            char_map_win[s[left]] -= 1
            if char_map_win[s[left]] <  char_map_t[s[left]]:
              match -= 1
            if char_map_win[s[left]] == 0:
              del char_map_win[s[left]]
          left += 1


    return s[res : res + res_len] if not math.isinf(res_len) else ""
      

        
        
        
    
    
        