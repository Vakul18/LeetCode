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
		
		
	
"""

class Solution:
	def partition_all(self, s: str) -> List[List[str]]:
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

	def partition(self, s : str) -> List[List[str]]:
		n = len(s)
		palindromesByRange = dict()
		partitions = self.findPalindromes(s, 0, n-1, len(s), palindromesByRange)
		result = [[ch for ch in s]]
		for partition in partitions:
			if len(partition) != len(s):
				result.append(partition)
		return result

	def findPalindromes(self, s:str, l : int, r : int, n : int, palindromesByRange : Dict[Tuple[int,int], List[List[str]]]) -> List[List[str]]:
		"""
		s : "aab"
		l = 0
		r = 2
		n = 3
		palindromesByRange = {{(2,2): ["b"]}, {(1,1) : ["a"]}}
		-- l = 1, r = 2
		"""
		if l > n or r < 0 or l > r:
			return []
		
		if (l,r) in palindromesByRange:
			return palindromesByRange[(l,r)]

		palindromeCombinations = []
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
			palindromeCombinations.append([s[l:r+1]])
		
		"""
		palindromeCombinations = []
		[]
	   
		   
		    
		"""
	
		rightPalindromeCombinations = []
		leftPalindromeCombinations = []
		for idx in range(l,r+1):
			rightList = self.findPalindromes(s, idx+1, r, n, palindromesByRange)
			leftList = self.findPalindromes(s, l, idx-1, n, palindromesByRange)

			if len(leftList) == 0 and len(rightList) > 0:
				for palindromes in rightList:
					palindromeCombinations.append([s[idx], *palindromes])
			elif len(rightList) == 0 and len(leftList) > 0:
				for palindromes in leftList:
					palindromeCombinations.append([*palindromes, s[idx]])

			else:
				for leftPalindrome in leftList:
					for rightPalindrome in rightList:
						palindromeCombinations.append([*leftPalindrome, s[idx], *rightPalindrome])
				

		palindromesByRange[(l,r)] = palindromeCombinations

		return palindromeCombinations

		
		




from typing import List



"""
s = "aab"
res= [["a", "a", "b"]]
path = []
part(0)
	index = 0
	i in (0-2) = 0
		isPalindrome(0,0) -> True
		

			

				

					
			
		
		
	

"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []


        def partitionHelper(index: int):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    partitionHelper(i + 1)
                    path.pop()


        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        partitionHelper(0)
        return res

class Solution:
	def __init__(self):
		self.path = []
		self.res = []

	def partition(self, s : str) -> List[List[str]]:
		self.s = s
		self.makePartitions(0)
		return self.res

	def makePartitions(self, index):
		if index == len(self.s):
			self.res.append(self.path[:])
			return
		for i in range(index, len(self.s)):
			if self.isPalindrome(index,i):
				self.path.append(self.s[index:i+1])
				self.makePartitions(i+1)
				self.path.pop()


	def isPalindrome(self, start, end):
		while start < end:
			if self.s[start] != self.s[end]:
				return False
			start += 1
			end -= 1

		return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return []

        cache = dict() # str -> partition

        def isPalindrome(t: str) -> bool:
            return t == t[::-1]
        
        def partitionRecurrsive(sub: str, c: dict) -> List[List[str]]:
            if len(sub) == 0:
                return [[]]
            res = []
            for i in range(len(sub)):
                left, right = sub[:i + 1], sub[i + 1:]
                if isPalindrome(left):
                    if not right in c:
                        c[right] = partitionRecurrsive(right, c)
                    for r in c[right]:
                        res.append([left] + r)
            return res
        
        return partitionRecurrsive(s, cache)
            


		
		

