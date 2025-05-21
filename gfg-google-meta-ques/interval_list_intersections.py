"""
Given two 2-D arrays which represent intervals. Each 2-D array represents a list of intervals. Each list of intervals is disjoint and sorted in increasing order. Find the intersection or set of ranges that are common to both the lists.
Note: Disjoint means no element is common in a list

Examples:

Input: a[][] = [[0, 4], [5, 10], [13, 20], [24, 25]], b[][] = [[1, 5], [8, 12], [15, 24], [25, 26]] 
Output: [[1, 4], [5, 5], [8, 10], [15, 20], [24, 24], [25, 25]]
Explanation: [1, 4] lies completely within the range [0, 4] and [1, 5]. Hence, [1, 4] is the desired intersection. Similarly, [24, 24] lies completely within two intervals [24, 25] and [15, 24]
Input: a[][] = [[0, 2], [5, 10], [12, 22], [24, 25]], b[][] = [[1, 4], [9, 12], [15, 24], [25, 26]]
Output: [[1, 2], [9, 10], [12, 12], [15, 22], [24, 24], [25, 25]]
Explanation: [1, 2] lies completely within the range [0, 2] and [1, 4]. Hence, [1, 2] is the desired intersection. Similarly, [12, 12] lies completely within two intervals [12, 22] and [9, 12]


a[][] = [[0, 9], [5, 10], [13, 20], [24, 25]], b[][] = [[1, 9], [8, 12], [15, 24], [25, 26]] 

[0, 11] [10, 11]

a_i      b_i

[[5, 9], ]

find if intersection is there

if a_i[0] <= b_i[1] or b_i[0] <= a_i[1]:
  intersection = [max(a_i[0], b_i[0]), min(a_i[1], b_i[1])]
if a_i[1] > b_i[1]:




"""

def findIntersection(arr1, arr2):
  i_1, i_2, n_1, n_2 = 0 , 0, len(arr1), len(arr2)
  intersection = []
  while i_1 < n_1 and i_2 < n_2:
    a, b = arr1[i_1], arr2[i_2]
    if a[1] >= b[0] and b[1] >= a[0]:
      intersection.append([max(a[0], b[0]), min(a[1], b[1])])
    if a[1] > b[1]:
      i_2 += 1
    elif b[1] > a[1]:
      i_1 += 1
    else:
      i_1 += 1
      i_2 += 1
  return intersection  
  