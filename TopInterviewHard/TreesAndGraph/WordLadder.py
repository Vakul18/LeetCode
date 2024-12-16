"""
Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

"""
from collections import deque

class Solution:
	

	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		wordsSet = set(wordList)
		if endWord not in wordsSet:
			return 0
		alreadyUsedWords = set()
		q = deque([(beginWord, 1)])
		while q:
			val, level = q.popleft()
			for charIdx in range(0,len(val)):
				for ch in string.ascii_lowercase:
					newString = val[:charIdx] + ch + val[charIdx+1:]
					if newString == endWord:
						return level + 1
					if newString not in alreadyUsedWords and newString  in wordsSet:
						q.append((newString, level + 1))
						alreadyUsedWords.add(newString)
					
		return 0
					
				
			
		
import queue

class Solution:
	
	class QueueNode:
		def __init__(self, val, level):
			self.val = val
			self.level = level
	

	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		wordsSet = set(wordList)
		if endWord not in wordsSet:
			return 0
		alreadyUsedWords = set()
		q = queue.Queue()
		q.put(self.QueueNode(beginWord, 1))
		while not q.empty():
			node = q.get()
			alreadyUsedWords.add(node.val)
			for charIdx in range(0,len(node.val)):
				for ch in range(0,26):
					newString = node.val[:charIdx] + chr(ch + ord('a')) + node.val[charIdx+1:]
					#print(newString)
					if newString == endWord:
						return node.level+1
					if newString in alreadyUsedWords or newString not in wordsSet:
						continue
					newNode = self.QueueNode(newString, node.level + 1)
					q.put(newNode)
					
		return 0
					
 