"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		max_len = 0
		max_substring = [0,0]
		for idx in range(0, n):
			(left, right) = self.check_palindrome(s, idx)
			curr_len = right - left + 1
			if max_len < curr_len:
				max_len = curr_len
				max_substring = [left, right]
		return s[max_substring[0] : max_substring[1] + 1]

	def check_palindrome(self, s, idx):
		# check even len palindome:
		left = idx
		right = idx + 1
		n = len(s)
		max_substring = [idx, idx]
		max_len = 1
		while left >= 0 and right < n and s[left] == s[right]:
			if max_len < right - left + 1:
				max_substring = [left, right]
				max_len = right - left + 1
			left -= 1
			right += 1
		
		# check odd len palindrome
		left = idx-1
		right = idx + 1
		while left >= 0 and right < n and s[left] == s[right]:
			if max_len < right - left + 1:
				max_substring = [left, right]
				max_len = right - left + 1
			left -= 1
			right += 1
		
		return (max_substring[0], max_substring[1])	
		
			
			
			
				