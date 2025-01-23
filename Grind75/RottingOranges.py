"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


0  1 0
0 -1 0
0  0 0 

|
1

queue : indices of bad oranges
iterate all matrix and fill queue
maintain time for till elements in the queue are processed,
then add the new rotten oragens to the queue and process again
return total time.

"""
