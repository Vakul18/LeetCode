"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import defaultdict
class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2) 
 
    if m < n:
      return False
 
    dict_s1 = defaultdict(int)
    for char in s1:
      dict_s1[char] += 1

    win = defaultdict(int)
    for idx in range(n):
      win[s2[idx]] += 1

    if win == dict_s1:
      return True

    for idx in range(n, m):
      win[s2[idx-n]] -= 1

      if win[s2[idx-n]] == 0:
        del win[s2[idx-n]]
  
      win[s2[idx]] += 1

      if win == dict_s1:
        return True

    return False



--------


from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        dict_s1 = defaultdict(int)
        for ch in s1:
            dict_s1[ch] += 1

        win = defaultdict(int)
        for i in range(n):
            win[s2[i]] += 1

        matches = sum(dict_s1[ch] == win[ch] for ch in dict_s1)

        for i in range(n, m):
            if matches == len(dict_s1):
                return True

            left_char, right_char = s2[i - n], s2[i]

            # Update left char
            if left_char in dict_s1:
                if win[left_char] == dict_s1[left_char]:
                    matches -= 1
                win[left_char] -= 1
                if win[left_char] == dict_s1[left_char]:
                    matches += 1

            # Update right char
            if right_char in dict_s1:
                if win[right_char] == dict_s1[right_char]:
                    matches -= 1
                win[right_char] += 1
                if win[right_char] == dict_s1[right_char]:
                    matches += 1

        return matches == len(dict_s1)


      
            