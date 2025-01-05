"""
Given a string s, your task is to find the longest palindromic substring within s. A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).

A palindrome is a string that reads the same forward and backwards. More formally, s is a palindrome if reverse(s) == s.

Note: If there are multiple palindromes with the same length, return the first occurrence of the longest palindromic substring from left to right.	

"zabba"
               0,4
     1,4         -       0,3
2,4       1,3          1,3 0,2
3,4 2,3  2,3 1,2     2,3 

0,4
0
"rnumsgyygo"
"ol"

(n-1) * 2
(n-2) * 4
(n-3) * 8
(n-4) * 16
|
(n- (n-1)) * 2^(n-1)

"""
from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s)-1
        queue = deque()  
        queue.append((left, right))  
        status = [[0 for i in range(0,right+1)] for j in range(0, right + 1)]

        while queue :
            left, right = queue.popleft()
            if s[left] == s[right]:
                self.check_palindrome(s, status, left, right)
                if status[left][right] == 1:
                    return s[left:right+1]
            
            if status[left][right-1] == 0:
                queue.append((left, right-1))
                
            if status[left+1][right] == 0:
                queue.append((left+1, right))                   
        
        return None

    def check_palindrome(self, s, status, left, right):
        if status[left][right] != 0:
            return
        l,r = left, right
        is_palindrome = True
        while l < r:
            if s[l] != s[r]:
                is_palindrome = False
                break
            l += 1
            r -= 1

        if is_palindrome:
            status[left][right] = 1
        else:
            status[left][right] = 2

        return
        
  
"hxhlx"         

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal_len = 0
        max_pal = (-1,-1)
        for idx in range(0, len(s)):
            (left, right) = self.max_palindrome_mid_at(s, idx)
            
            if right - left + 1 > max_pal_len:
                max_pal_len = right - left + 1
                max_pal = (left, right)
            
        
        return s[max_pal[0]: max_pal[1]+1]
 
    def max_palindrome_mid_at(self, s, idx):
        n = len(s)

        left = idx - 1
        right = idx + 1
        
        odd_left, odd_right = self.check_max_palindrome(s, left, right)

        odd_len = odd_right - odd_left + 1

        if idx + 1 < n and s[idx] == s[idx + 1]:
            left = idx - 1
            right = idx + 2
            even_left, even_right = self.check_max_palindrome(s, left, right)
            even_len = even_right - even_left + 1
            if even_len > odd_len:
                return even_left, even_right

        return odd_left, odd_right
        
    def check_max_palindrome(self, s, left, right):
        n = len(s)
        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            
            left -= 1
            right += 1
        left = left + 1
        right = right - 1
        return left,right
                     
                
