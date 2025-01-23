"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

left = 6, right = 6, max_area = 49
(4)*5 = 20

"""

class Solution:
	def maxArea(self, arr: List[int]) -> int:
		left = 0
		right = len(arr)-1
		max_area = 0
		while left < right:
			area = min(arr[left], arr[right])*(right-left)
			max_area  = max(area, max_area)
			if arr[right] < arr[left]:
				right -= 1
			else:
				left += 1
		return max_area



class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            current_l, current_r = height[i], height[j]
            max_water = max(max_water, (j - i) * min(current_l, current_r))
            if current_l < current_r:
                while i < j and height[i] <= current_l:
                    i += 1
            else:
                while i < j and height[j] <= current_r:
                    j -= 1
        return max_water