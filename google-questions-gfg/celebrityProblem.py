"""
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.  A square matrix mat (n*n) is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.


0 1
0 0

[]
 0 : 1 

"""

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        possible_celebs = []
        follower = [0 for _ in range(0,n)]

        for i in range(0,n):
            known_people = 0
            for j in range(0,n):
                if i == j:
                    continue
                known_people += mat[i][j]
                follower[j] += mat[i][j]
            if known_people == 0:
                possible_celebs.append(i)

        for celeb in possible_celebs:
            if follower[celeb] == n-1:
                return celeb

        return -1       