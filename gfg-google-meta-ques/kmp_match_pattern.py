"""
a a a c a a a

0 1 2 0 1 2 3
"""

class Solution:
  def search(self, pat, txt):
    m , n = len(pat), len(txt)
    lps = [0] * m

    def compute_lps(m):
    
      pre_idx , suff_idx = 0, 1

      while suff_idx < m:
        if pat[pre_idx] == pat[suff_idx]:
          pre_idx += 1
          lps[suff_idx] = pre_idx
          suff_idx += 1
        else:
          if pre_idx == 0:
            lps[suff_idx] = 0
            suff_idx += 1
          else:
            pre_idx = lps[pre_idx-1]
    
    compute_lps(m)
    i, j = 0 , 0
    result = []
    while i < n:
      if pat[j] == txt[i]:
        i += 1
        j += 1
        if j == m:
          result.append(i - m)
          j = lps[j-1]
      else:
        if j == 0:
          i += 1
        else:
          j = lps[j-1]

    return result
          
          
  