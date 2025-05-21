"""
670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

2 7 3 6

"""
class Solution:
  def maximumSwap(self, num: int) -> int:
    ls = list(str(num))
    n = len(ls) 
    suff = [-1] * n
    suff[n-1] = n-1
    max_num = int(ls[n-1])
    for i in range(n-2, -1, -1):
      if int(ls[i]) > max_num:
        suff[i] = i
        max_num = int(ls[i])
      else:
        suff[i] = suff[i+1]

    for i in range(n):
      max_idx = suff[i]
 
      if int(ls[i]) < int(ls[max_idx]):
        ls[i], ls[suff[i]] = ls[suff[i]], ls[i]
        break

    return int(''.join(ls)) 
    	