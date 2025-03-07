"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


arr = [2,1,3], target = 6 -> []
arr = [1,2,3,4], target = 4 -> [[1,3], [4]]

dp[i][j] = subsets with sum j for arr[0] - arr[i]

dp[i][0] = 1
dp[0][arr[0]] = [arr[0]]

for i in (0,n)
	for j in (1,target+1)
		if arr[i] <= j
			taken_comb = [sublist + [element] for sublist in dp[i-1]][j-arr[i]]
		not_taken_comb = sublist in dp[i-1]][j][:]

		dp[i][j] = taken_comb + not_taken_comb

return dp[n][target]



[[[], [], [2], []],
 [[], [], [], []],
 [[], [], [], []],
 [[], [], [], []],
 [[], [], [], []],
 [[], [], [], []],
 [[], [], [], []],
 [[], [], [], []]]


[2,7] -> 7

dp = [
[[],[],[[2]],[],[],[],[],[]], 
[[],[],[],[],[],[],[],[[7]]]
]

i = 1,j = 7
cand[i] = 7


[[[[]], [[]], [[2]], [[]], [[]], [[]], [[]], [[]]],
 [[[]], [[]], [[]], [[3]], [[]], [[]], [[]], [[]]], 
[[[]], [[]], [[]], [[]], [[]], [[]], [[6]], [[]]],
 [[[]], [[]], [[]], [[]], [[]], [[]], [[]], [[7]]]]




"""
# This program finds all combinations without duplicates
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		n = len(candidates)
		dp = [[(False, None) for _ in range(0,target+1)] for _ in range(0, n)]
		#print(dp)
		for i in range(0,n):
			if candidates[i] <= target:
				dp[i][candidates[i]] = (True, [[candidates[i]]])


		for i in range(1,n):
			for j in range(1,target+1):
				taken_comb = None
				if candidates[i] <= j and dp[i-1][j-candidates[i]][0]:
					#print(f'i : {i}, j: {j} ,  j- : {j-candidates[i]}, dp : {dp[i-1][j-candidates[i]]}')
					taken_comb = []
					for sublist in dp[i-1][j-candidates[i]][1]:
						taken_comb.append(sublist[:] + [candidates[i]])	
					#print(f'taken: {taken_comb}')

				
				not_taken_comb = dp[i-1][j][1][:] if dp[i-1][j][0] else None

				#print(f'nit taken: {not_taken_comb}')
				
				if taken_comb and not_taken_comb:
					dp[i][j] = (True, taken_comb + not_taken_comb)
				elif not_taken_comb:
					dp[i][j] = (True, not_taken_comb)
				elif taken_comb:
					dp[i][j] = (True, taken_comb)
		if dp[n-1][target][0]:
			return dp[n-1][target][1]
		else:
			return []


# program to find all combinations with duplicates
"""
[2,3,6,7], 7

[[[[]], True], 
[[[]], False],
[[[], [2]], True],
 [[[], [3]], True], 
[[[], [2], [2, 2]], True],
 [[[], [2], [3, 2], [3], [2, 3]], True],
 [[[], [2], [2, 2], [2, 2, 2], [3], [3, 3], [6]], True],
 [[[], [2], [2, 2], [3, 2, 2], [3, 2], [2, 3, 2], [3], [2, 3], [2, 2, 3], [7]], True]]

[[[[]], True],
 [[[]], False],
 [[[], [2]], True], 
[[[], [3]], True], 
[[[], [2], [2, 2]], True], 
[[[], [2], [3, 2], [3], [2, 3]], True],
 [[[], [2], [2, 2], [2, 2, 2], [3], [3, 3], [6]], True],
 [[[], [2], [2, 2], [3, 2, 2], [3, 2], [2, 3, 2], [3], [2, 3], [2, 2, 3], [7]], True]]


"""
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		dp = [[] for _ in range(target+1)]
		dp[0] = [[]]
		for curr_target in range(1, target+1):
			for num in candidates:
				left_target = curr_target - num
				if left_target >= 0:
					for sublist in 	dp[left_target]:
						dp[curr_target].append(sublist + [num])
		s = set()
		res = []
		for ls in dp[target]:
			sorted_tuple = tuple(sorted(ls))
			if sorted_tuple not in s:
				res.append(ls)	
				s.add(sorted_tuple)			
		return res




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(start, remain, cur_res):
            
            if remain == 0:
                result.append(cur_res[:])
                return
            
            for i in range(start, len(candidates)):
                
                if candidates[i] > remain:
                    break
                
                cur_res.append(candidates[i])

                backtrack(i, remain - candidates[i], cur_res)
                cur_res.pop()
 

        backtrack(0, target, [])

        return result			


