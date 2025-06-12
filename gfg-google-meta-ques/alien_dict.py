"""
Alien Dictionary

A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

Examples:

Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "bdac".
The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
So, 'b' → 'd' → 'a' → 'c' is a valid ordering.
Input: words[] = ["caa", "aaa", "aab"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "cab".
The pair "caa" and "aaa" suggests 'c' appears before 'a'.
The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
So, 'c' → 'a' → 'b' is a valid ordering.
Input: words[] = ["ab", "cd", "ef", "ad"]
Output: ""
Explanation: No valid ordering of letters is possible.
The pair "ab" and "ef" suggests "a" appears before "e".
The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.
Constraints:
1 ≤ words.length ≤ 500
1 ≤ words[i].length ≤ 100
words[i] consists only of lowercase English letters.
"""
from collections import deque, defaultdict
class Solution:
  def findOrder(words):
    adj = defaultdict(list)
    n = len(words)
    exists = [0] * 26

    for word in words:
      for char in word:
        exists[ord(char)-ord('a')] = 1
    indeg = [0] * 26
    for i in range(n-1):
      word1 = words[i]
      word2 = words[i + 1]

      idx = 0
      while idx < len(word1) and idx < len(word2):
        if word1[idx] == word2[idx]:
          idx += 1 
          continue
        u = ord(word1[idx]) - ord('a')
        v = ord(word2[idx]) - ord('a')
        adj[u].append(v)
        indeg[v] += 1

        break
      else:
        if len(word1) > len(word2):
          return ""

      
    topo = []
    queue = deque()
    for idx in range(26):
      if exists[idx] == 1 and indeg[idx] == 0:
        queue.append(idx)

    while queue:
      u = queue.popleft()
      topo.append(chr(u + ord('a')))
      for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
          queue.append(v)
      
     
    if (len(topo) == sum(exists)):
      return "".join(topo)
    else:
      return ""
    
if __name__ == "__main__":
    words = ["dddc", "a", "ad", "ab", "b", "be", "cd", "cded"]
    solution = Solution()
    result = Solution.findOrder(words)
    print(result)  # Output: "wertf"

      
        

      






    
