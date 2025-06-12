"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

from collections import defaultdict

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s_char = defaultdict(int)
    t_char = defaultdict(int)

    for char in s:
      s_char[char] += 1

    for char in t:
      t_char[char] += 1

    return s_char == t_char