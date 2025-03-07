"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.


Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.


"""

class Solution:
	def longestPalindrome(self, s: str) -> int:
		char_counts = [0 for _ in range(0,58)]
		
		pal_count = 0
		n = len(s)

		for char in s:
			char_idx = ord(char) - ord('a')
			char_counts[char_idx] += 1
			if char_counts[char_idx]%2 == 0:
				pal_count += 2

		if pal_count < n:
			return pal_count + 1
		else:
			return pal_count