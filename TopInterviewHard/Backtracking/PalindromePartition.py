"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

"abaca"

[a, b, c, a, aba, aca]

"ababa"


["ababa", "aba", "a", "b", "bab", "aba"]
0,4

0,3
	0,2
		0,1
			0,0
			1,1
		1,2
			1,1
			2,2	
	1,3
		1,2
		2,3
			2,2
			3,3
		


1,4
	1,3
	2,4
		2,3
		3,4
			3,3
			4,4
		
		
	
"ababa"

[[ababa], ]
ababa

abab a






"""

class Solution:
	def partition(self, s: str) -> List[List[str]]:
		n = len(s)
		palindromes = set()
		l = 0
		r = n-1
		toBeProcessed = [(0,n-1)]
		alreadyProcessed = [[False for _ in range(n)] for _ in range(n)]
		while(len(toBeProcessed)>0):
			(l,r) = toBeProcessed.pop()
			
			isPalindrome = True
			left = l
			right = r
			while(left<right):
				if s[left] != s[right]:
					isPalindrome = False
					break
				
				left+=1
				right-=1

			if isPalindrome:
				palindromes.add(s[l:r+1])

			if l+1 < n and not alreadyProcessed[l+1][r]:
				toBeProcessed.append((l+1, r))
			if r-1 > -1 and not alreadyProcessed[l][r-1]:
				toBeProcessed.append((l, r-1))

		return palindromes	
		

class Solution:
	def partition(self, s: str) -> List[List[str]]:
		
		
		

