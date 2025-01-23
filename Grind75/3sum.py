"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


[1, 2, 2, 3, -4] -> [[1,3,-4], [2,2,-4]]

indices_by_val = [(1,0), (2,[1,2]), (3,3), (-4,4)]

result : []
"""

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		indices_by_val = dict()
		used_values = set() 
		for idx in range(0, len(nums)):
			if nums[idx] not in indices_by_val:
				indices_by_val[nums[idx]] = idx
		
		result = []
		for i in range(0, len(nums)-1):
			for j in range(i+1, len(nums)):
				if -(nums[i] + nums[j]) in indices_by_val and (nums[i], nums[j]) not in used_values and (nums[j], nums[i]) not in used_values:
					k =  indices_by_val[-(nums[i] + nums[j])]
					if i != k and j!=k:
						result.append([nums[i],nums[j],nums[k]])
						used_values.update([(nums[i],nums[j]), (nums[j],nums[i]), (nums[k],nums[j]), (nums[j],nums[k]), (nums[k],nums[i]), (nums[i],nums[k])])

		return result



O(n^2)

###################################################

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		sorted_nums = sorted(nums)
		
		n = len(sorted_nums)
		result = []
		idx = 0
		while idx < n-2:
		
			curr_target = sorted_nums[idx]
			left = idx + 1
			right = n-1

			while left < right:
				sum = sorted_nums[left] + sorted_nums[right] 
				if sum  == -curr_target:
					result.append([sorted_nums[idx], sorted_nums[left], sorted_nums[right]])
					left_val = sorted_nums[left]
					right_val = sorted_nums[right] 
					while left < right and sorted_nums[left] == left_val:
						left += 1

					while right > left and sorted_nums[right] == right_val:
						right -= 1
			
				elif sum > -curr_target:
					right -= 1
				else:
					left += 1


			while idx < n-2 and sorted_nums[idx] == curr_target:
				idx += 1							
			

		return result
 




#####################################3

























		
		
		