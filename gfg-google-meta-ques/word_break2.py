"""
Given a string s and a dictionary dict[] of valid words, you need to return all possible ways to break the string s into sentence such that each word in the sentence is a valid dictionary word.
You are allowed to use a valid word multiple times in the sentence.

Examples:

Input: s = "likegfg", dict[] = ["lik", "like", "egfg", "gfg"]
Output: 
"lik egfg"
"like gfg"
Explanation: All the words in the given sentences are present in the dictionary.
Input: s = "geeksforgeeks", dict[] = ["for", "geeks"]
Output: "geeks for geeks"
Explanation: The string "geeksforgeeks" can be broken into valid words from the dictionary in one way.
Constraints:
1 ≤ dict.size() ≤ 20
1 ≤ dict[i] ≤ 15
1 ≤ s.size() ≤ 500

time : O(k*n^2)
space : O(n*k)
"""
#User function Template for python3

class Solution:
  def wordBreak(self, dict, s):
    n = len(s)
    dp = [[] for _ in range(n+1)]
    dp[0] = [[]]
    for i in range(n):
      for word in dict:
        word_start_idx = i - len(word) + 1
        if word_start_idx >= 0 and (s[word_start_idx: i + 1] == word):
          for ls in dp[word_start_idx]:
            dp[i+1].append(ls + [word])

    return [' '.join(ls) for ls in dp[n]]


###################

# Python program to find valid word breaks
# using tabulation

def wordBreak(dict, s):

    st = set(dict)
    n = len(s)

    # dp[i] stores all valid sentences
    # starting from index i
    dp = [[] for _ in range(n + 1)]

    # Base case: an empty string at the end
    dp[n].append("")

    for i in range(n - 1, -1, -1):

        # Check substrings starting from the
        # current index
        for j in range(i + 1, n + 1):
            word = s[i:j]

            # Check if the word exists in the
            # dictionary
            if word in st:

                # Append valid sub-sentences to
                # the current word
                for sub in dp[j]:
                    if sub:
                        dp[i].append(word + " " + sub)
                    else:
                        dp[i].append(word)

    return dp[0]


if __name__ == '__main__':

    s = "likegfg"
    dict = ["lik", "like", "egfg", "gfg" ]

    result = wordBreak(dict, s)

    for sentence in result:
        print(sentence)
        