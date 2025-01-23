"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
"abc", "bca" -> true
"abc", "ca" -> false
"", "c" -> true
"aa", "ab" -> false
"""

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		countByCharsMag = dict()
		for c in magazine:
			if c in countByCharsMag:
				countByCharsMag[c] += 1
			else:
				countByCharsMag[c] = 1

		for c in ransomNote:
			if c not in countByCharsMag or countByCharsMag[c] == 0:
				return False
			countByCharsMag[c] -= 1

		return True