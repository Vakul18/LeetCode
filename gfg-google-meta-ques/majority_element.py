"""
Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.
Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than 1/2 times, so it is the majority element.
Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than 2/2 times, so there is no majority element.
"""
class Solution:
  def majorityElement(self, arr):
    n = len(arr)
    if n == 0:
      return -1

    curr_maj, count = arr[0], 1

    for i in range(1, n):
      if arr[i] == curr_maj:
        count += 1
      else:
        count -= 1
        if count == 0:
          curr_maj = arr[i]
          count = 1
    count = 0
    for num in arr:
      if num == curr_maj:
        count += 1

    return curr_maj if count > (n/2) else -1
    