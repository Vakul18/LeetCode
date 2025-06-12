"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Input: strs = ["eet", "ete", "abc"]

Output: [["eet","ete"], ["abc"]]


"""
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = dict()

    for s in strs:
      str_s = ''.join(sorted(s, key = lambda x : ord(x)))
      if str_s in anagram_map:
        anagram_map[str_s].append(s)
      else:
        anagram_map[str_s] = [s]

    return list(anagram_map.values())
    
    
        