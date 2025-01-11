"""
Given two strings s1 and s2. Find the smallest window in the string s1 consisting of all the characters(including duplicates) of the string s2. Return "-1" in case no such window is present. If there are multiple such windows of the same length, return the one with the least starting index.
Note: All characters are in lowercase letters.

Scenarios:

s1 = abdef
s2 = ae

4 : abde

s1 = a
S2 = ae

-1

s1 = 123456
s2 = a

-1

s1 : abcdef
s2 : aabb

-1

s1 = hxdaafhaghb
s2 = ah

ha

h-x-d-a --
a-a-f-h --
a-f-h --
h-a --
a-

"""

    class Window:
    	def __init__(self, start, pattern, char):
    		self.start_idx = start
    		self.end_idx = start
    		self.chars = {char}
    		self.pattern = pattern
    	
    	def add(self, char):
    		self.end_idx += 1
    		if char in self.pattern:
    			self.chars.add(char)
    			if len(self.chars) == len(self.pattern):
    				return True
    		
    		return False
    		
    	def length(self):
            return self.end_idx - self.start_idx + 1
    	
    						
    		
    
    def smallestWindow(self, s1, s2):
    	pattern_len = len(s2)
    	pattern = set(s2)
    	windows = []
    	best_window = ''
    	best_window_len = sys.maxsize
    	win_idx_to_skip = set()
    	
    	for idx, value in enumerate(s1):
    		c = s1[idx]
    		for win_idx, window in enumerate(windows):
    			if win_idx in win_idx_to_skip:
    				continue;
    
    			if window.add(c):
    				win_idx_to_skip.add(win_idx)
    				if window.length() < best_window_len :
    					best_window = s1[window.start_idx: 1 + window.end_idx]
    					
    					if window.length() == len(pattern):
    						return best_window
    					
    					best_window_len = window.length()
    		
    		if c in pattern:
    			windows.append(Solution.Window(idx, pattern, c))
    	
    			
    	if not best_window:
    		return -1
    	else:
    		return best_window



// Binary search approach

class Solution:
    def isValid(self,s, p, mid):
    # Count the frequency of each character in p
        count = [0] * 256
        distinct = 0
    
        # Count the frequency of each character in p
        for x in p:
            if count[ord(x)] == 0:
                distinct += 1
            count[ord(x)] += 1
    
        # Stores the number of characters in a substring of size
        # mid in s whose frequency is the same as the frequency in p
        curr_count = 0
        start = -1
        for i in range(len(s)):
            count[ord(s[i])] -= 1
            if count[ord(s[i])] == 0:
                curr_count += 1
    
            # Slide the window: remove the effect of the character that is out of the current window
            if i >= mid:
                count[ord(s[i - mid])] += 1
                if count[ord(s[i - mid])] == 1:
                    curr_count -= 1
    
            # Check if the current window contains all characters of p
            if i >= mid - 1:
                if curr_count == distinct:
                    start = i - mid + 1
                    return True, start
    
        return False, start
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        m = len(s)
        n = len(p)
    
        # If s is smaller than p, it's impossible
        if m < n:
            return "-1"
    
        minLength = float('inf')
    
        # Lower bound and Upper Bound for Binary Search
        # The smallest valid window size is n (size of p)
        low, high = n, m
    
        # Stores starting index of the min-length substring
        idx = -1
    
        # Applying Binary Search on the answer
        while low <= high:
            mid = (low + high) // 2
            valid, start = self.isValid(s, p, mid)
    
            # If a substring of length mid is found which
            # contains all the characters of p, then
            # update minLength and high, otherwise update low
            if valid:
                if mid < minLength:
                    minLength = mid
                    idx = start
                high = mid - 1
            else:
                low = mid + 1
    
        if idx == -1:
            return "-1"
    
        return s[idx:idx + minLength]
				

					
// two pointer approach with sliding window

class Solution:
    # Function to find the smallest window in the string s1 consisting
    # of all the characters of string s2.
    def smallestWindow(self, s1: str, s2: str) -> str:
        if not s1 or not s2:
            return "-1"

        # Dictionary to keep a count of all the unique characters in s2.
        phash = defaultdict(int)
        for char in s2:
            phash[char] += 1

        # Number of unique characters in s2 that need to be present in the desired window.
        required = len(phash)

        # Left and Right pointers
        left, right = 0, 0

        # formed is used to keep track of how many unique characters in s2
        # are present in the current window in its desired frequency.
        formed = 0

        # Dictionary to keep a count of all the unique characters in the current window.
        window_counts = defaultdict(int)

        # (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s1):
            character = s1[right]
            window_counts[character] += 1

            # If the current character's frequency matches its frequency in s2, increment formed.
            if character in phash and window_counts[character] == phash[
                    character]:
                formed += 1

            # Try and contract the window till the point it ceases to be 'desirable'.
            while left <= right and formed == required:
                character = s1[left]

                # Save the smallest window until now.
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in phash and window_counts[character] < phash[
                        character]:
                    formed -= 1

                left += 1

            # Keep expanding the window once we are done contracting.
            right += 1

        if ans[0] == float("inf"):
            return "-1"
        else:
            return s1[ans[1]:ans[2] + 1]
			
					
					
				
			
		
		
	

