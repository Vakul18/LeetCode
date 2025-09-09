"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
"""
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    window = dict()
    len_longest = 0
    win_l = 0

    for idx, char in enumerate(s):
      if char in window and window[char] >= win_l:
        win_l = window[char] + 1

      window[char] = idx
      len_longest = max(len_longest, idx - win_l + 1)

    return len_longest
    
    
        