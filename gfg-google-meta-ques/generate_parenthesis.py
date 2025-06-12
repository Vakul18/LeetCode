"""
Generate Parentheses

Given a number n, return all the combinations of balanced parentheses of length n.
Note: A sequence of parentheses is balanced if every opening bracket has a corresponding closing bracket in the correct order.
For example, "(())", "()()", and "(()())" are balanced, whereas ")()(", "))((", and "()))" are not.

Input: n = 6
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Explanation: These are the only possible valid balanced parentheses.


Input: n = 4
Output: ["(())", "()()"]
Explanation: These are the only possible valid balanced parentheses.

n=2
()

n = 4

(()), ()()


n = 6

(()())

3 ,3

(

2,3

()

2,2
()


"""
#User function Template for python3

class Solution:
  def generateParentheses(self, n):

    combinations = []
    
    def create(open_count, close_count, parenthesis_list):
      if close_count == 0:
        combinations.append(''.join(parenthesis_list))
        return
       
      if open_count < close_count:
        parenthesis_list.append(')')
        create(open_count, close_count - 1, parenthesis_list)
        parenthesis_list.pop()


      if open_count > 0:
        parenthesis_list.append('(')
        create(open_count -1 , close_count, parenthesis_list)
        parenthesis_list.pop()
     
    create(n//2, n//2, [])
    return combinations
        




