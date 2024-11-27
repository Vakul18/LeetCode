"""
Given a string, find all palindrom subsequences.

"axbxdabx" -> [a, x, b, d, aba, xax, xxx, aa, xx, , axa, axxa,xbx, xdx,xbbx]

"axbx" -> [a,x,b,xbx,xx]

[]

 axbx
xbx abx axx axb




"axbx"

"""

class Palindrome:
	def GetAllPalindromSubsequences(self, string : str) -> list[str]:
		processed_strings = set()
		string_process_stack = [string]
		result = []
		
		"""
		result = [a, x]
		processed_strings = [axbx, axb, ax, x, a]
		string_process_stack = ["xbx", "abx", "axx", "xb", "ab"]
		curr_string = 
		l_idx = 0 
		r_idx = 0

		
		"""
		#process for palidrome till stack is empty
		while(len(string_process_stack) > 0):
			
			curr_string = string_process_stack.pop()

			if curr_string in processed_strings:
				continue
		
			#if string is palindrome, add to result
			l_idx = 0
			r_idx = len(curr_string)-1
			is_palindrome = True
			while(l_idx < r_idx):
				if curr_string[l_idx] != curr_string[r_idx]:
					is_palindrome = False
					break
				l_idx += 1
				r_idx -= 1

			if is_palindrome:
				result.append(curr_string)
			
			#mark string as processed
			processed_strings.add(curr_string)
			
			if len(curr_string) == 1:
				continue
			
			# remove each char from string and add to stack		
			for idx in range(len(curr_string)):
				new_string = curr_string[:idx] + curr_string[idx+1:]
				string_process_stack.append(new_string)

				

		return result	


a = Palindrome()
op = a.GetAllPalindromSubsequences("axbx")
print(op)			







		