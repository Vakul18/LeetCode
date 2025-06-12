"""
Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find the length of the shortest transformation sequence from startWord to targetWord.
Keep the following conditions in mind:

A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList
The second part of this problem can be found here.

Note: If no possible way to transform sequence from startWord to targetWord return 0

Input:
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der", targetWord= "dfs",
Output:
3
Explanation:
The length of the smallest transformation
sequence from "der" to "dfs" is 3
i,e "der" -> "dfr" -> "dfs".


Input:
wordList = {"geek", "gefk"}
startWord = "gedk", targetWord= "geek", 
Output:
2
Explanation:
gedk -> geek


Input: 
wordList = {"poon", "plee", "same", "poie","plea","plie","poin"}
startWord = "toon", targetWord= "plea",
Output: 7 
Explanation:
toon -> poon -> poin -> poie -> plie -> plee -> plea 
 

"""
from collections import deque, defaultdict
class Solution:
  def ladderLength(self, startWord, targetWord, wordList):
    graph = defaultdict(list)
    wordSet = set(wordList)
    if targetWord not in wordSet:
      return 0

    if startWord not in wordSet:
      wordList = wordList + [startWord]

    # prepare graph of word transformations
    for word in wordList:
      for word_idx in range(len(word)):
        for ch_idx in range(26):
          new_word = word[:word_idx] + chr(ch_idx + ord('a')) + word[word_idx+1:]
          if new_word in wordSet:
            graph[word].append(new_word)

    
    queue = deque([startWord])
    visited = set([startWord])
    transform_count = 0
    while queue:
      size = len(queue)
      transform_count += 1
      for _ in range(size):
        curr_word = queue.popleft()

        for connect_word in graph[curr_word]:
          if connect_word in visited:
            continue

          if connect_word == targetWord:
            return transform_count + 1

          visited.add(connect_word)
          queue.append(connect_word)
        
    return 0
    
    