"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""
from collections import deque
class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
   
    if endWord not in wordSet:
      return 0

    queue = deque([(beginWord, 1)])
    
    while queue:
      word, steps = queue.popleft()
      if word == endWord:
        return steps

      for idx in range(len(word)):
        for chIdx in range(26):
          transformed_word = word[:idx] + chr(ord('a') + chIdx) + word[idx+1:]
          if transformed_word in wordSet:
            queue.append((transformed_word, steps + 1))
            wordSet.remove(transformed_word)

    return 0


--------------------------------


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        m = len(beginWord)
        wordSet = set(wordList)
        que = deque([(beginWord, 1)])

        while que:
            tmp_word, step = que.popleft()

            for i in range(m):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = tmp_word[:i] + c + tmp_word[i+1:]

                    if new_word == endWord:
                        return step + 1

                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        que.append((new_word, step + 1))
        return 0
 

    
    
 

    
    
        