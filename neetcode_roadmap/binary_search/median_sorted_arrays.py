"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums2) < len(nums1):
      nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)

    total_left = (m + n + 1)//2
    
    l, r = 0, m
 
    while l <= r:
      i  = (l + r)//2
      j = total_left - i 

      max_left1 = float('-inf') if i == 0 else nums1[i-1]
      min_right1 = float('inf') if i == m else nums1[i]

      max_left2 = float('-inf') if j == 0 else nums2[j-1]
      min_right2 = float('inf') if j == n else nums2[j]


      if max_left2 <= min_right1 and max_left1 <= min_right2:
        if (m+n)%2 == 0:
          return (max(max_left2, max_left1) + min(min_right1, min_right2))/2
        else:
          return max(max_left2, max_left1)
      elif max_left1 > min_right2:
        r = i - 1
      else:
        l = i + 1


------------


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # keep nums1 smallest
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            middle = (left + right) // 2
            j = half - middle - 2

            nums1_left = nums1[middle] if middle >= 0 else float("-inf")
            nums1_right = nums1[middle + 1] if middle + 1 < len(nums1) else float("inf")
            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)

            if nums1_left > nums2_right:
                right = middle - 1
            else:
                left = middle + 1

  
        
