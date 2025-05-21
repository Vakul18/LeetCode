"""
Two strings are called k-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most k characters in a string.

Given two strings of lowercase alphabets and an integer value k, the task is to find if two strings are k-anagrams of each other or not.
"""
#User function template for Python 3
from collections import defaultdict
class Solution:
  def areKAnagrams(self, s1, s2, k):
    if len(s1) != len(s2):
      return False
    dict1  = defaultdict(int)
    dict2 = defaultdict(int)

    for c in s1:
      dict1[c] += 1

    for c in s2:
      dict2[c] += 1

    diff = 0
    for key, val in dict1.items():
      if key in dict2:
        diff += max(val - dict2[key], 0)
      else:
        diff += val
      if diff > k:
        return False

    return True


###################################################


from collections import defaultdict
class Solution:
  def areKAnagrams(self, s1, s2, k):
    if len(s1) != len(s2):
      return False
    dict1  = defaultdict(int)


    for c in s1:
      dict1[c] += 1

    for c in s2:
      if dict1[c] > 0:
        dict1[c] -= 1

    diff = sum(dict1.values())
    return diff <= k

      
       