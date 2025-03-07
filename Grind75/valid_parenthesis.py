"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

"""

class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) == 0:
			return True
		stack = []
		parenthesis_match_map = {")":"(", "}":"{", "]":"["}
		for char in s:
			if len(stack)>0 and char in  parenthesis_match_map and parenthesis_match_map[char] == stack[-1]:
				stack.pop()
			else:
				stack.append(char)

		return len(stack) == 0
			
			
        	 