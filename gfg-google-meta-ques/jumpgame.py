"""
Given a array of positive integers arr, where each element denotes the maximum length of jump you can cover. Find out if you can make it to the last index starting from the first index of the list, return true if you can reach the last index.
"""
class Solution:
  # Function to check if we can reach the last index from the 0th index.
  def canReach(self, arr):
    max_reach = arr[0]
    idx, n = 1, len(arr)
    while idx <= max_reach and max_reach < n-1:
      max_reach = max(max_reach, idx + arr[idx])
      idx += 1

    return max_reach >= n-1
    