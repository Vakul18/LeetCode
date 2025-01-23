"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

s : "abcabcbb" -> abc
s : "xsaqwsssa" -> xsaqw

"""

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		char_dict = dict()
		max_len = 0
		curr_left_idx = 0

		for idx in range(0, len(s)):
			c = s[idx]
			if c in char_dict and char_dict[c] >= curr_left_idx:
				c_idx = char_dict[c]
				curr_left_idx = c_idx + 1
			
			char_dict[c] = idx
			max_len = max(max_len, idx - curr_left_idx + 1)
		return max_len	
			