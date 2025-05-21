"""
Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

Two strings s1 and s2 are called shifted if the following conditions are satisfied:

s1.length = s2.length
s1[i] = s2[i] + m for 1 <= i <= s1.length  for a constant integer m
"""
from collections import defaultdict
class Solution:
  def groupShiftedString(self, arr):
    dict = defaultdict(list)

    for s in arr:
      disp = ord(s[0]) - ord('a')
      base_char = []
      for c in s:
        c_d = ord(c) - disp
        if c_d < ord('a'):
          c_d += 26

        base_char.append(chr(c_d))
      base_str = ''.join(base_char)
      dict[base_str].append(s)

    return list(dict.values())