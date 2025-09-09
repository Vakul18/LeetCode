"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    unwind_arr = []

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        unwind_arr.append(matrix[i][j])

    def binary_search(arr : List[int], target):
      l, r = 0, len(arr) - 1
      while l<=r:
        m = (l+r)//2

        if arr[m] == target:
          return m

        if target > arr[m]:
          l = m + 1
        else:
          r = m - 1

      return -1

    result = binary_search(unwind_arr, target)

    return False if result == -1 else True 



--------------------------------



from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1

    while l <= r:
      mid = (l + r) // 2
      row, col = mid // n, mid % n
      val = matrix[row][col]

      if val == target:
        return True
      elif val < target:
        l = mid + 1
      else:
        r = mid - 1

    return False


    
    
        