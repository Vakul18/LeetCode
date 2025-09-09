"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

(()(()))
((((
n = 2
(
n = 1
 /    \
((     ()
n = 0   n = 0

"""
class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    answer = []

    def generate(res : List[str], l):
      if len(res) == 2*n:
        answer.append(res)
        return
  
      if l > 0:
        res.append(')')
        generate(res, l - 1)
        res.pop()

      res.append('(')
      generate(res, l + 1)
      res.pop()        
              
    

    generate(['('], 1)

    return answer


    

    
        