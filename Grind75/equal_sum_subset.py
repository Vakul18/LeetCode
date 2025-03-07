"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
nums = [1,5,11,5] -> [1, 5, 5, 11]

[11], [5, 5]

sum1 = 11

sum2 = 11


nums = [3,3,3,4,5]

sum1 = 8
sum2 = 10

nums = [1,1,1,2,2,2]


nums = [1,1,2,2]


nums = [1,1]

1. calculate total sum
2. not divisible by 2, return false
3. else set target = total sum /2
4. return true of there exists subset with sum == target


nums = [1,1,1,2,2,2]


dp[i][j] : can we create j by summing a subset 0 -> i



"""

class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		total_sum = sum(nums)

		if total_sum%2 != 0:
			return False

		target = total_sum//2

		return self.canHaveSum(nums, target)


	def canHaveSum(self, nums, target):
		n = len(nums)
		dp = [[False for _ in range(target+1)] for _ in range(n)]

		for idx in range(n):
			dp[idx][0] = True

		if nums[0] <= target:
			dp[0][nums[0]] = True

		for idx in range(1,n):
			for sum in range(1, target+1):
				taken_result = False
				if sum >= nums[idx]:
					taken_result = dp[idx-1][sum-nums[idx]]
				not_taken_result = dp[idx-1][sum]
				dp[idx][sum] = taken_result or not_taken_result

		return dp[n-1][target]	


class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		total_sum = sum(nums)

		if total_sum%2 != 0:
			return False

		target = total_sum//2

		return self.canHaveSum(nums, target)


	def canHaveSum(self, nums, target):
		n = len(nums)
		dp = [[False for _ in range(target+1)] for _ in range(n)]

		for idx in range(n):
			dp[idx][0] = True
		for idx in range(n):
			if nums[idx] <= target:
				dp[idx][nums[idx]] = True

		for idx in range(1,n):
			for sum in range(1, target+1):
				taken_result = False
				if sum >= nums[idx]:
					taken_result = dp[idx-1][sum-nums[idx]]
				not_taken_result = dp[idx-1][sum]
				dp[idx][sum] = taken_result or not_taken_result

		return dp[n-1][target]		


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1:
            return False
        s //= 2

        # dp = [False] * (s+1)
        dp = 1

        # nums.sort()

        for num in nums:
            dp |= dp << num
        
        return bool(dp & 1 << s)			

