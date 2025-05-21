"""
Stickler the thief wants to loot money from the houses arranged in a line. He cannot loot two consecutive houses and aims to maximize his total loot.
Given an array, arr[] where arr[i] represents the amount of money in the i-th house.
Determine the maximum amount he can loot.


Input: arr[] = [6, 5, 5, 7, 4]
Output: 15
Explanation: Maximum amount he can get by looting 1st, 3rd and 5th house. Which is 6 + 5 + 4 = 15.
Input: arr[] = [1, 5, 3]
Output: 5
Explanation: Loot only 2nd house and get maximum amount of 5.
Input: arr[] = [4, 4, 4, 4]
Output: 8
Explanation: The optimal choice is to loot every alternate house. Looting the 1st and 3rd houses, or the 2nd and 4th, both give a maximum total of 4 + 4 = 8.

9 4 11 12 6 12


"""
class Solution:  
  def findMaxSum(self,arr):
    dp = [0] * (len(arr) + 1)

    dp[1], dp[2] = arr[0], arr[1]
    max_loot = max(dp[0], dp[1], dp[2])
    for idx in range(2, len(arr)):
      dp[idx+1] = arr[idx] + max(dp[idx-1], dp[idx-2])
      max_loot = max(max_loot, dp[idx+1])
    return max_loot



#######################

class Solution:  
  def findMaxSum(self,arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])

    # Initialize dp array
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    # Fill dp array using recurrence relation
    for i in range(2, n):
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

    return dp[n - 1]