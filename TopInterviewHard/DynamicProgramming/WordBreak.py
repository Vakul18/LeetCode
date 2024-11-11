"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


"abckabc"
{"abc", "kabc", "ab"}

0,0 : false
0,1 : false
0,2 : true
3,3
3,4
...
3,6 : true

0,2 : 3

dp[0-n]  = false
i n-1 to 0
	for word in dict
		if s[i:i+len(word)-1] == word and dp[i+len(word)-1]):
			dp[i] = true
			break

return dp[0]


"abckabc"
{"abc", "kabc", "ab"}

n=7
dp[f,f,f,f,t,f,f,t]

idx = 6
idx = 5
idx=3


"""

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		n = len(s)
		dp = [False for i in range(n+1)]
		dp[n] = True
		
		for idx in range(n-1,-1,-1):
			for word in wordDict:
				if (idx+len(word)-1 < n) and (s[idx:idx+len(word)] == word) and dp[idx+len(word)]:
					dp[idx] = True
					break
		return dp[0]
		
		