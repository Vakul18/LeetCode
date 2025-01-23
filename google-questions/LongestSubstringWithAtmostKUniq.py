"""
Longest substring with atmost K distinct characters from the given set of characters

aabcdffjk 2

aab

abbbbbbc
3

"""
def is_valid(char_count, k):
	count = 0
	for i in range(0,26):
		if char_count[i] > 0:
			count += 1
	return (count <= k)

def kDistinctChars(k, str):
	char_count = [0] * 26
	
	if k > len(str):
		return -1

	left = 0
	right = 0
	best_size = 0
	best_start_idx = -1
	
	while right < len(str) and left >= right:
		char_count[ord(str[right]) - ord('a')] += 1
		
		is_valid_win = is_valid(char_count, k)
		if is_valid_win and best_size < (right - left +1):
			best_size = right - left +1
			best_start_idx = left
		while not is_valid(char_count, k):
			char_count[ord(str[left]) - ord('a')] -= 1
			left += 1
		right += 1

	return best_size
		
		
	

