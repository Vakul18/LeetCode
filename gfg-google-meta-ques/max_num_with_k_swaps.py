"""
Largest number in K swaps
Difficulty: MediumAccuracy: 18.84%Submissions: 121K+Points: 4Average Time: 30m
Given a number k and string s of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of s at most k times.

Examples :

Input: s = "1234567", k = 4
Output: 7654321
Explanation: Three swaps can make the input 1234567 to 7654321, swapping 1 with 7, 2 with 6 and finally 3 with 5.
Input: s = "3435335", k = 3
Output: 5543333
Explanation: Three swaps can make the input 3435335 to 5543333, swapping 3 with 5, 4 with 5 and finally 3 with 4.
Input: s = "1034", k = 2
Output: 4301
Explanation: Two swaps can make the input 1034 to 4301, swapping 1 with 4 and finally 0 with 3. 


Input: s = "1234567", k = 4
Output: 7654321
7234561 -> 7634521 -> 7654321  

Input: s = "3416527", k = 4
3416527 -> 7416523 -> 7614523 -> 7654123 -> 7654321

Input: s = "3416527", k = 3
6413527 -> 7413526 -> 7613524 -> 7653124
           6473521 -> 6473521

1100909, k = 1

9921100
   1120909
 /        \
9120109   9120901
"""
class Solution:
  def findMaximumNum(self, s, k):
    max_num = [int(s)]
    number = [int(_) for _ in s]
    
    def findMax(index, swaps):
      if index == len(s) or swaps == 0:
        num = int(''.join(map(str,number))) 
        if  num > max_num[0]:
          max_num[0] = num
        return

      max_digit = max(number[index:])

      if number[index] == max_digit:
        findMax(index+1, swaps)
        return

      for j in range(index+1, len(number)):
        if number[j] != max_digit:
          continue

        number[j], number[index] = number[index], number[j]
        
        findMax(index+1, swaps -1)

        number[j], number[index] = number[index], number[j]

      return
    
    findMax(0, k)
    return max_num[0]

