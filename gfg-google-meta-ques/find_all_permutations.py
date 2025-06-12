"""
Given an array arr[] of length n. Find all possible distinct permutations of the array in sorted order. A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.
[1, 2, 3]
1,2,3 1,3,2 2,1,3 2,3,1 3,1,2 3,2,1
"""
#User function Template for python3

class Solution:
  def uniquePerms(self, nums):
    perms = []
    n = len(nums)
    visited = [False] * n
    nums_s = sorted(nums)

    def search(path, n):
      if len(path) == n:
        perms.append(path[:])
        return

      for idx in range(n):
        if visited[idx] or (idx > 0 and nums_s[idx-1] == nums_s[idx] and visited[idx-1]):
          continue

        visited[idx] = True
        path.append(nums_s[idx])
        search(path, n)
        path.pop()
        visited[idx] = False
           
    search([], n)
    return perms
    