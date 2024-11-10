"""
1 3 2

c[0] = 1
c[1] = 2 (1 3, 13)
i =2 , 2
c[2] = c[1]

1 2 3

c[0] = 1
c[1] = 2 (1 2, 12)
i =2 , 2
c[2] = c[1] + c[0] (1 2, 12, 1 23)

1 2 0
c[0] = 1
c[1] = 2 (1 2, 12)
c[2] =   (1 20)


226
n=3
c= [1,2,3]


301
n=3
c = [1,0,0]



		
	
27
	

"""
class Solution:
	def numDecodings(self, a: str) -> int:
		if int(a[0]) == 0:
			return 0
		n = len(a)
		if n == 1:
			return 1
		
		c = [0] * n
		c[0] = 1
		c[1] = 0
		
		if int(a[0] + a[1]) <= 26:
			if int(a[1])!=0:
				c[1] = 2
			else:
				c[1] = 1
		elif int(a[1]) != 0:
			c[1] = 1
		

		for i in range(2,n):
			if int(a[i]) != 0:
				c[i] = c[i-1]
		
			else:
				if int(a[i-1]) == 0:
					return 0

			if int(a[i-1] + a[i]) <= 26 and int(a[i-1]) !=0:
				c[i] += c[i-2]
		return c[n-1]



################################################################################

class Solution:
    def numDecodings(self, s: str) -> int:
        # Base case
        # Only one way to make a group beyond the end of the string (do nothing)
        # Empty string
        dp = {len(s) : 1}

        # Iterate backwards bc each state depends on future states (bottom up)
        for i in range(len(s) - 1, -1, -1):
            # If the digit = 0 or start of two digits = 0
            # Cannot be valid -> 0 ways to group
            if s[i] == "0":
                dp[i] = 0
            # Digit = [1, 9]
            # Single digit case
            # Equals next dp since one digit can always be counted as it's own group
            # so dp[i] will be AT LEAST dp[i + 1]
            else:
                dp[i] = dp[i + 1]

            # Two digit decode
            # Check if current digit + next digit form a valid two digit number
            # If so, add it's dp as well
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        
        # How many ways can we decode it starting at index 0
        return dp[0]

"""
dp[i] = dp[i + 1] (decode cur as one digit) + dp[i + 2] (decode cur as two digits)

Time complexity: O(n)
Space complexity: O(n)
"""