"""
Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.
Constraints:
1 ≤ |s| ≤ 105 
1 <= k <= 100


abc3[b2[ca]]abc -> abc

st : [(a,1), (b,1), (c,1), ('bcacabcacabcaca', 1), (a, 1), (b, 1), (c, 1)] 

pop till 2
['a', 'c']
loop in reverse the whole array 2 times

pop till 3
['caca', 'b']
lopp in reverse 3 times
bcacabcacabcaca

abc3[b2[ca]]abc
""
a1[a]b
"""


class Solution:
  def decodedString(self, s):
    st = []
    idx = 0
    n = len(s)
    """
    s = abc10[b2[ca]]abc
    n = 16
    idx = 11
    st = [(a, F), (b, F), (c, F), (bcaca*10)]
    """
    while idx < n:
      char = s[idx]
      if ord(char) >= ord('a') and ord(char) <= ord('z'): ### char found
        st.append((char, False))
      elif char.isdigit(): ### k found
        num = [char] # num = 1
        while idx+1 < n and s[idx+1].isdigit():
          num.append(s[idx+1])
          idx = idx + 1
        st.append(((int)(''.join(num)), True))
      elif char == ']': ### end of encoded string
        char_ls = [] # [caca, b]
        while st:
          element = st.pop() # (c, F)
          if element[1]:
            k = element[0]
            string = ''.join(char_ls[::-1])
            string = string * k
            st.append((string, False))
            break
          else:
            char_ls.append(element[0])
      idx += 1
    result = ''.join(map(lambda x : x[0], st))
    return result

    
      
    