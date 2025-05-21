"""
Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.

n = 4, k = 10
a[] = [1, 2, 3, 4]
Output : 
7


a[] = [1, 2, 3, 4, 1, 5]
count = 1- 1+(2*1)=3- 1+(3*2)=7-  
curr_prod = 2
"""
class Solution:
  def countSubArrayProductLessThanK(self, arr, n, k):
    start_win = 0
    count = 0
    curr_prod = 1
    i = 0
    
    while i < n:
      curr_prod *= arr[i]
      
      while curr_prod >= k and start_win <= i:
        curr_prod /= arr[start_win]
        start_win += 1

      no_of_elements = i - start_win + 1

      if no_of_elements > 0:
        count += no_of_elements

      i += 1

    return count