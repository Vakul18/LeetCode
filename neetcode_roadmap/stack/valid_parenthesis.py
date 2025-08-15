"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


"""
class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) == 0:
      return True
    open_brackets = set(['(', '{', '['])
    close_brackets = {')' : '(', '}' : '{', ']' : '['}
   
    st = []

    for char in s:
      if char in open_brackets:
        st.append(char)
      elif char in close_brackets:
        if not st:
          return False
        last_char = st.pop()
        matching_char = close_brackets[char]
        if last_char != matching_char:
          return False
      else:
        return False

    return True if not st else False
        
    

    
      

    
    