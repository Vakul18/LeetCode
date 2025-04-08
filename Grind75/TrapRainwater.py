"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105	


[0,1,0,2,1,0,1,3,2,1,2,1]
 |                   


find max rl[]
for each idx 
 v = min(max_left, max_rl[idx + 1])
 water += v - height[idx]
 max_left = max(max_left, height[idx])




[4,2,0,3,2,5]
max_rl = []
water = 

"""

class Solution:
	def trap(self, height: List[int]) -> int:
		n = len(height)
		max_rl = [0 for _ in range(0,n)]
		max_rl[n-1] = height[n-1]
		max_h = height[n-1]
		for idx in range(n-2 ,-1, -1):
			max_h = max(height[idx], max_h)
			max_rl[idx] = max_h
		max_water = 0
		max_l = height[0]
		for idx in range(1,n-1):
			possible_water = min(max_l, max_rl[idx+1]) - height[idx]
			max_l = max(height[idx], max_l)
			if possible_water > 0:
				max_water += possible_water

		return max_water



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        left = 0
        right = n - 1
        totalWater = 0
        maxLeft = height[left] # track max heights from left
        maxRight = height[right] # track max heights from right

        # process until pointers meet
        while left < right:
            if maxLeft < maxRight:
                # left side is lower, process left pointer
                left += 1
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    totalWater += (maxLeft - height[left])
            else:
                # right side is lower, process right pointer
                right -= 1
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    totalWater += (maxRight - height[right])
        return totalWater




        

		
			
		