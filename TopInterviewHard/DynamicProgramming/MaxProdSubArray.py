"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

2 4 -3 5 -9 10

p[i,j]
p[i, j+1] = p[i,j] * a[j+1]
p[i+1,j] = p[i,j] * a[i+1]
p[i+1, j+1] = p[i,j] * a[i+1] * a[j+1]

   2 4 -3 5 -9 10
2  
4  
-3
5
-9
10

prod1 = 2
prod2 = 2
result = 2

i  = 1 , 4
temp = max(8, 4, 8) = 8
prod2 = 4
prod1  = 8
result = 8

i=2, -3
temp = max(-24, -3, -12) = -3
prod2 = -24
prod1  = -3
result = 8

i=3, 5
temp = max(-15, 5, -120) = 5
prod2 = -120
prod1  = 5
result = 8

i=4, -9
temp = max(-45, -9, 1080) = 1080
prod2 = -45
prod1  = 1080
result = 1080

i=5, 10
temp = max(10800, 10, -450) = 10800
prod2 = -450
prod1  = 1080
result = 1080

"""
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0
		
		prod1 = nums[0]
		prod2 = nums[0]
		result = nums[0]
		
		for i in range(1, len(nums)):
			temp = max(prod1 * nums[i], nums[i], prod2*nums[i])
			prod2 = min(prod1 * nums[i], nums[i], prod2*nums[i])
			prod1 = temp

			if prod1 > result:
				result = prod1

		return result



#########################################################################################################

"""
-1 5 9 10
n = 6





"""


class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		pre = 1
		suff = 1
		result = float('-inf')
		n = len(nums)
		for i in range(n):
			if pre == 0:
				pre = 1

			if suff == 0:
				suff = 1

			pre *= nums[i]
			suff *= nums[n-i-1]
			
			result = max(result, pre, suff)


		return result




















			