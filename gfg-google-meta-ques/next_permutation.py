"""
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]

2, 4, 1, 7, 5, 0
      |     

2, 4, 5, 7, 1, 0



0 1 2 4 5 7

0 1 2 4 7 5

0 1 2 5 4 7

0 1 2 5 7 4

0 1 2 7 4 5

0 1 2 7 5 4

0 1 4 2 5 7

0 1 4 5 2 7

0 1 4 5 7 2




7 5 4 2 1 0

--
4 3 1 2
    |    


[2, 4, 3, 7, 2, 8]
             |  





[2, 4, 7, 3, 8, 2]
                |      


"""
class Solution:
  def nextPermutation(self, arr):
    k, n = -1, len(arr)
    
    for idx in range(n-2, -1, -1):
      if arr[idx] < arr[idx + 1]:
        k = idx
        break

    if k == -1:
      arr.sort()
      return arr

    l = -1
    for idx in range(n-1, k, -1):
      if arr[idx] > arr[k]:
        l = idx
        break
    arr[l], arr[k] = arr[k], arr[l]
    arr[k+1:] = reversed(arr[k+1:])
    return arr    