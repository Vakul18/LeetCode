"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


"2" : ["a", "b" , "c"]
...

string = "234"

prevString = ["a", "b", "c"]
idx = 1
digit = 3
digitChars = ["d", "e", "f"]
curr_strings = ["ad", "ae", "af", "bd"]


"""

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if len(digits) == 0:
			return []
		num_to_char = {"":[], "2" : ["a", "b", "c"], "3" : ["d", "e", "f"], "4" : ["g", "h", "i"], "5" : ["j", "k", "l"], "6" : ["m", "n", "o"], 
				"7" : ["p", "q", "r", "s"], "8" : ["t", "u", "v"], "9" : ["w", "x", "y", "z"]} 
		prev_strings = num_to_char[digits[0]]
		for idx in range(1, len(digits)):
			digit = digits[idx]
			digitChars = num_to_char[digit]
			curr_strings = []
			for string in prev_strings:
				for digitChar in digitChars:
					#print(f"{string}, {digitChar}")
					curr_strings.append(str(string + digitChar))

			prev_strings = curr_strings

		return prev_strings
			