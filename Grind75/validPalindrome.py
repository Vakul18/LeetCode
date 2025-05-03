"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"A man, a plan, a canal: Panama"
      |                   |

"  "
"""
class Solution:
  def isPalindrome(self, s: str) -> bool:
    n = len(s)
    l,r = 0, n-1
    s = s.lower()
    while l<=r:
      while l < r and not s[l].isalnum():
        l += 1
      while l < r and not s[r].isalnum():
        r -= 1
      if s[l] != s[r]:
        return False

      l += 1
      r -= 1

    return True
      

-----------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(filter(str.isalnum, s)).lower()
        # cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        if cleaned_s== cleaned_s[::-1]:
            return True
        else:
            return False
      
        