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
  def generateParenthesis(self, n: int) -> List[str]:
    answer = []

    def generate(res : List[str], o, c):
      if len(res) == 2*n:
        answer.append("".join(res))
        return
  
      if c < o:
        res.append(')')
        generate(res, o, c + 1)
        res.pop()
      if o < n:
        res.append('(')
        generate(res, o + 1, c)
        res.pop()        
              
    

    generate([], 0, 0)

    return answer




        
    

    
      

    
    