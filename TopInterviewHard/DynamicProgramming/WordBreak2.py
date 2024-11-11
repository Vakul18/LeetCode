"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"abckabc"
{"abck", "kabc", "abc"} -> {abc, kabc},{abck abc}

dp { [[abc],[kabc]],[],[],[[kabc]],[[abc]],[],[],[]}



idx 3


	
	


"""

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		n = len(s)
		dp = [[] for i in range(n+1)]
		#print(dp)
		dp[n] = [[]]
		for idx in range(n-1,-1,-1):
			for word in wordDict:
				if (idx+len(word)-1 < n) and (s[idx:idx+len(word)] == word) and len(dp[idx+len(word)])>0:
					for wordList in dp[idx+len(word)]:
						newList = wordList + [word]
						#print(newList)
						dp[idx].append(newList)
		output = [' '.join(sentence[::-1]) for sentence in dp[0]]
		return output