"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

[1,2,2,2,1] -> 2

maj_elem = 2
maj_elem_count = 3
curr_elem = 1
curr_elem_count = 1

[1,2,2,1]


[1,3,3,2]
[1,1,3,3,3]

[2,2,1,1,1,2,2]

[3,2,3]

[1,3,1,1,4,1,1,5,1,1,6,2,2]

"""
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return None
		count = 1
		maj_elem = nums[0]
		
		for idx in range(1, len(nums)):
			num = nums[idx]
			if num == maj_elem:
				count += 1
			else:
				count -= 1
				if count <= 0:
					maj_elem = num
					count = 1

		return maj_elem
				
