"""
Given an array containing distinct integers, find the number of surpassers for each of its elements.

An element y is said to be the surpasser of element x if it is a greater element on the right of x. ie if x = arr[i] and y = arr[j], i<j and arr[i] < arr[j]. 
Input: arr[] = [4, 5, 1, 2, 3]
Output: [1, 0, 2, 1, 0]
Explanation: There are no elements greater than 3 at the right of 3. There is one element at right of 2 and greater than 2. There are 2 elements greater than 1 at the right of 1. And so on.
Input: arr[] = [2, 7, 5, 3, 8, 1]
Output: [4, 1, 1, 1, 0, 0]

[4, 5, 1, 2, 3]

[1,2,3,4,5]


[2, 7, 5, 3, 8, 1]


[2, 7, 5], [3, 8, 1]

[2, 7], [5], [3, 8], [1]
[2], [7],      [3], [8]




"""
class Solution:
  def findSurpasser(self, arr):
    
    count = [0] * len(arr)
    val_map = {}
    for i, num in enumerate(arr):
      val_map[num] = i

    def merge_sort(l , r):
      if l == r:
        return 
      
      
      m = (l+r)//2

      merge_sort(l, m)
      merge_sort(m+1, r)

      a = arr[l:m+1]
      b = arr[m+1:r+1]

      a_i, b_i = 0, 0
      i = l
      while a_i < len(a) and b_i < len(b):
        if a[a_i] < b[b_i]:
          arr[i] = a[a_i]
          count[val_map[a[a_i]]] += len(b) - b_i
          a_i += 1
          
        else:
          arr[i] = b[b_i]
          b_i += 1
        i += 1

      while b_i < len(b):
        arr[i] = b[b_i]
        b_i += 1
        i += 1

      while a_i < len(a):
        arr[i] = a[a_i]
        a_i += 1
        i += 1

      return
    merge_sort(0, len(arr)-1)
    return count
          


      	
      





    
    