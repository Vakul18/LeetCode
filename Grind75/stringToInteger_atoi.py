"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""
class Solution:
	def myAtoi(self, s: str) -> int:
		n = len(s)
		integer = 0
		start = -1
		end = -1
		max_size = 2**31-1
		min_size = -2**31
		for idx in range(0, n):
			c = s[idx]
			if c == '-' or c == '+':
				if start == -1:
					start = idx
					end = idx
				else:
					end = idx

			if ord(c)>=48 and ord(c)<=57:
				if start == -1:
					start = idx
					end = idx
				else:
					end = idx
				print(s[start : end+1])
				integer  = int(s[start : end+1])
				if integer >= max_size:
					return max_size
				elif integer <= min_size:
					return min_size

		return integer

class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        idx = 0
        
        # Skip leading whitespace
        while idx < n and s[idx] == ' ':
            idx += 1
            
        if idx == n:
            return 0
        
        # Handle sign
        sign = 1
        if s[idx] == '-' or s[idx] == '+':
            sign = -1 if s[idx] == '-' else 1
            idx += 1

        # Convert digits to integer
        integer = 0
        while idx < n and '0' <= s[idx] <= '9':
            digit = ord(s[idx]) - ord('0')
            # Check for overflow
            if integer > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            integer = integer * 10 + digit
            idx += 1
        
        return sign * integer

				
		