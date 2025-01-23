"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["le", "leet","code"]
Output: true
n = 8, dp = [T,F,T,F,F,F,F,F,F]
idx = 3, word = leet

"""

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		n = len(s)
		dp = [False] * (n+1)
		dp[0] = True
		
		for idx in range(1,n+1):
			for word in wordDict:
				if idx-len(word) >= 0 and (s[idx-len(word):idx] == word):
					dp[idx] = dp[idx-len(word)]
				if dp[idx]:
					break

		return dp[n]