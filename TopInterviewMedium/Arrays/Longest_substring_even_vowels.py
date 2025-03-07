"""
Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

"eleetminicoworoep" 
"eleete"

"""
class Solution:
	def findTheLongestSubstring(self, s: str) -> int:
		
		max_len = 0
		vowels = {'a' : 1, 'e' : 2, 'i' : 4, 'o' : 8, 'u' : 16}
		xor_val = 0
		seen = {0 : -1}
		
		for idx, char in enumerate(s):
			if char in vowels:
				xor_val ^= vowels[char]
			
			if xor_val in seen:
				max_len = max(max_len, idx - seen[xor_val])
			else:
				seen[xor_val] = idx
			
			

		return max_len


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for char in s:

            if char in vowels:
                vowels[char] += 1

        max_len = 0

        for right in range(len(s) - 1, -1, -1):                
            curr_vowels = vowels.copy()
            left = 0

            while (left <= right
                and any(v % 2 == 1 for v in curr_vowels.values())):
                
                if s[left] in vowels:
                    curr_vowels[s[left]] -= 1

                left += 1
            
            max_len = max(max_len, right - left + 1)

            if max_len >= right:
                return max_len

            if s[right] in vowels:
                vowels[s[right]] -= 1