"""
Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters

Note: While forming a word we can move to any of the 8 adjacent cells. A cell can be used only once in one word.

Example 1:

Input: 
N = 1
dictionary = {"CAT"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}
Output:
CAT
Explanation: 
C A P
A N D
T I E
Words we got is denoted using same color.
Example 2:

Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3 
board = {{G,I,Z},{U,E,K},{Q,S,E}}
Output:
GEEKS QUIZ
Explanation: 
G I Z
U E K
Q S E 
Words we got is denoted using same color.

####################################
dictionary = {"CAT", "CAP"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}

#
c
a
t p


"""
#User function Template for python3
class Node:
  def __init__(self):
    self.children = dict()
    self.isEnd = False

  def addChild(self, letter):
    if letter not in self.children:
      self.children[letter] = Node()
    return self.children[letter]   


class Solution:
  def wordBoggle(self,board,dictionary):
    trie = Node()
    
    for word in dictionary:
      curr_node = trie
      for char in word:
        childNode = curr_node.addChild(char)
        curr_node = childNode
      curr_node.isEnd = True
    r, c = len(board), len(board[0])
    visited = [[False  for _ in range(c)] for _ in range(r)]
    
    def searchWords(i, j, r, c, trie_node, found_letters):      
      found_letters.append(board[i][j])
      curr_node = trie_node.children[board[i][j]]
      
      if curr_node.isEnd:
        words.add(''.join(found_letters))

      adj_cells_off = [-1, 0, 1]
      
      for x_off in adj_cells_off:
        for y_off in adj_cells_off:
          x, y = i + x_off, j + y_off
         
          if x < 0 or y < 0 or x >= r or y >= c or visited[x][y] or board[x][y] not in curr_node.children:
            continue
          
          visited[x][y] = True
          found = searchWords(x, y, r, c, curr_node, found_letters)

          visited[x][y] = False

      found_letters.pop()
      return
          
    words = set()
    for i in range(r):
      for j in range(c):  ## i, j = 0, 0, board[i][j] = C
        if board[i][j] not in trie.children:
          continue
        
        visited[i][j] = True
       
        searchWords(i, j, r, c, trie, [])

        visited[i][j] = False
 
        if len(words) == len(dictionary):
          break
      if len(words) == len(dictionary):
        break

    return sorted(list(words))


    
    