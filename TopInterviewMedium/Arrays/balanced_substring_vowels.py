"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

"cccleetcode"

max_len = 0
vow = 0, cons = 0
i = 1
j = 1

char = c

"""



class Solution:
	def findTheLongestSubstring(self, s: str) -> int:
		max_len = 0
		n = len(s)
		vowels = set(['a', 'e', 'i', 'o', 'u'])
		for i in range(0, n-1):
			no_vowels = 0
			no_cons = 0
			for j in range(i, n):
				char = s[j]
				if char in vowels:
					no_vowels += 1
				else:
					no_cons += 1

				if no_vowels == no_cons:
					#print(f's : {s[i:j+1]}, vowel : {no_vowels}, cons : {no_cons}, i : {i}, j : {j}')
					max_len = max(max_len, j-i+1)

		return max_len


"""
seen = {0:-1, -1:0}
max_len = 0
balance = -1
s = "cccleetcode"
i = 0 , char = c

"""

def longest_substring_equal_vowels_consonants(s: str) -> int:
    # A set of vowels
    vowels = set('aeiouAEIOU')
    
    # Dictionary to store the first occurrence of a specific balance (difference between vowels and consonants)
    seen = {0: -1}
    
    max_len = 0
    balance = 0  # Keeps track of the difference between vowels and consonants
    
    for i, char in enumerate(s):
        # If the character is a vowel, increase balance by 1
        if char in vowels:
            balance += 1
        # If the character is a consonant, decrease balance by 1
        elif char.isalpha():  # Only consider alphabetic characters
            balance -= 1
        
        # If this balance has been seen before, calculate the length of the substring
        if balance in seen:
            max_len = max(max_len, i - seen[balance])
        else:
            # Store the first occurrence of this balance
            seen[balance] = i
    
    return max_len


        