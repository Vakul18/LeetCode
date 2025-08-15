"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


"""
class Solution:
  def isPalindrome(self, s: str) -> bool:
    n = len(s)
    l, r = 0, n-1

    while l <= r:
      if not s[l].isalnum():
        l += 1
      elif not s[r].isalnum():
        r -= 1
      elif s[l].lower() == s[r].lower():
        l+=1
        r-=1
      else:
        return False

    return True