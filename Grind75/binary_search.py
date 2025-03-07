"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

[0, 23, 24, 25], 25
left = 3 , right = 3
mid = 2

"""
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		n = len(nums)
		left, right = 0, n-1

		while left <= right:
			mid = (left + right)//2

			if nums[mid] == target:
				return mid

			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1

		return -1