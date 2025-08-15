"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
from typing import List
class Solution:

  def encode(self, strs: List[str]) -> str:
    result = []
    for string in strs:
      result.append(f'#{len(string)}#{string}')

    return ''.join(result)
    
    

  def decode(self, s: str) -> List[str]:
    idx = 0
    s_l = len(s)
    decoded_str = []
   
    while idx < s_l:
      if s[idx] == '#':
        string = []
        idx += 1
        l = int(s[idx])
        idx += 1
        while s[idx] != '#':
          l = l*10 + int(s[idx])
          idx += 1
        
        for _ in range(l):
          idx += 1
          string.append(s[idx])
        decoded_str.append(''.join(string))
      else:
        raise ValueError('invalid value')
      idx += 1

    return decoded_str


######################################################################

from typing import List
class Solution:

  def encode(self, strs: List[str]) -> str:
    result = []
    for string in strs:
      result.append(f'#{len(string)}#{string}')

    return ''.join(result)

  def decode(self, s: str) -> List[str]:
    idx = 0
    decoded_str = []
   
    while idx < len(s):
        if s[idx] == '#':
            idx += 1
            length_str = ''
            while s[idx] != '#':
                length_str += s[idx]
                idx += 1
            length = int(length_str)
            idx += 1  # Skip the second '#'
            string = s[idx:idx+length]
            decoded_str.append(string)
            idx += length
        else:
            raise ValueError('Invalid encoding format')
    
    return decoded_str

