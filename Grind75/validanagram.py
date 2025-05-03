"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    n_s, n_t = len(s), len(t)
    if n_s != n_t:
      return False

    s_char_map = dict()
    t_char_map = dict()

    for idx in range(n_s):
      s_char_map[s[idx]] = s_char_map.get(s[idx], 0) + 1
      t_char_map[t[idx]] = t_char_map.get(t[idx], 0) + 1

    return s_char_map == t_char_map
    