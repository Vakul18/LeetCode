"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple subsets of the largest size, return the lexicographically greatest array after sorting it in ascending order.

Input: arr[] = [1, 2, 3, 6]
Output: [1, 3, 6]
Explanation: The largest divisible subset can be either [1, 2, 6] or [1, 3, 6], both having a length of 3. However, [1, 3, 6] is lexicographically greater than [1, 2, 6], so it is the correct output.

Input: arr[] = [1, 2, 4, 8]
Output: [1, 2, 4, 8]
Explanation: The largest divisible subset is [1, 2, 4, 8], where each element divides the next one. This subset is already the lexicographically greatest.

Input: arr[] = [3, 5, 10, 20, 21]
Output: [5, 10, 20]
Explanation: The largest divisible subset is [5, 10, 20], where each element is divisible by the previous one. Other valid subsets like [3] or [21] are smaller in size.


1 2 3 6




"""
class Solution:
  def largestDivisibleSubset(self, arr):
    n = len(arr)
    arr_s = sorted(arr)
    dp = [[arr_s[i]] for i in range(n)] 
    
    max_list = dp[n-1]
    #print(dp)
    for i in range(1, n):
      for j in range(i-1, -1, -1):
        if arr_s[i] % arr_s[j] == 0 and len(dp[i]) < (len(dp[j]) + 1):
          dp[i] = dp[j] + [arr_s[i]] 
          
      if len(dp[i]) > len(max_list):
        max_list = dp[i]
      elif len(dp[i]) == len(max_list):
        k = 0
        while k < len(max_list):
          if dp[i][k] > max_list[k]:
            max_list = dp[i]
            break
          elif dp[i][k] == max_list[k]:
            k += 1
          else:
            break

      

    return max_list


#################################
class Solution:
  def largestDivisibleSubset(self, arr):
    arr_s = sorted(arr, reverse = True)
    n = len(arr)
    next = [-1] * n
    dp = [1]* n
    max_idx = 0
    max_size = 1
    for i in range(1, n):
      for j in range(i):
        if arr_s[j] % arr_s[i] == 0 and dp[i] < dp[j] + 1:
          dp[i] = dp[j] + 1
          next[i] = j

      if max_size < dp[i]:
        max_idx = i
        max_size = dp[i]

    k = max_idx
    result = []
    while k!= -1:
      result.append(arr_s[k])
      if k == next[k]:
        break
      k = next[k]

    return result

      
   


           