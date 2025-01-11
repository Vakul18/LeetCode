"""
Given a string you need to print longest possible substring that has exactly M unique characters. If there is more than one substring of longest possible length, then print any one of them.

aabcfg 3
aabc

aaabbbccc 4
aaabbbccc

a 1
a

"""
class Solution:

        def longestKSubstr(self, s, k):
    	if len(s) < k :
    		return -1
    
    	left = 0
    	right = 0
    	unique_char = dict()
    	best_size = 0
    	substring = ''
    	
    	while right < len(s) and left <= right:
    		count = unique_char.get(s[right])
    		if count is None:
    			unique_char[s[right]] = 1
    		else:
    			unique_char[s[right]] += 1
    
    		if(len(unique_char) == k and best_size < (right - left + 1)):
    			best_size = (right - left + 1)
    			substring = s[left : right + 1]
    		elif (len(unique_char) > k):
    			unique_char[s[left]] -= 1
    			if unique_char[s[left]] == 0:
    				unique_char.pop(s[left])
    			left += 1
    		right += 1
    	
    	if not substring:
    		return -1
    	else:
    		return best_size
	
	
			





# Python program to find the longest substring with k unique 
# characters in a given string 
MAX_CHARS = 26
 
# This function calculates number of unique characters 
# using a associative array count[]. Returns true if 
# no. of characters are less than required else returns 
# false. 
def isValid(count, k): 
    val = 0
    for i in range(MAX_CHARS): 
        if count[i] > 0: 
            val += 1
 
    # Return true if k is greater than or equal to val 
    return (k >= val) 
 
# Finds the maximum substring with exactly k unique characters 
def kUniques(s, k): 
    u = 0 # number of unique characters 
    n = len(s) 
 
    # Associative array to store the count 
    count = [0] * MAX_CHARS 
 
    # Traverse the string, fills the associative array 
    # count[] and count number of unique characters 
    for i in range(n): 
        if count[ord(s[i])-ord('a')] == 0: 
            u += 1
        count[ord(s[i])-ord('a')] += 1
 
    # If there are not enough unique characters, show 
    # an error message. 
    if u < k: 
        print ("Not enough unique characters")
        return
 
    # Otherwise take a window with first element in it. 
    # start and end variables. 
    curr_start = 0
    curr_end = 0
 
    # Also initialize values for result longest window 
    max_window_size = 1
    max_window_start = 0
 
    # Initialize associative array count[] with zero 
    count = [0] * len(count) 
 
    count[ord(s[0])-ord('a')] += 1 # put the first character 
 
    # Start from the second character and add 
    # characters in window according to above 
    # explanation 
    for i in range(1,n): 
 
        # Add the character 's[i]' to current window 
        count[ord(s[i])-ord('a')] += 1
        curr_end+=1
 
        # If there are more than k unique characters in 
        # current window, remove from left side 
        while not isValid(count, k): 
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1
 
        # Update the max window size if required 
        if curr_end-curr_start+1 > max_window_size: 
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start 
 
    print ("Max substring is : " + s[max_window_start:max_window_start  + max_window_size] 
    + " with length " + str(max_window_size))	



