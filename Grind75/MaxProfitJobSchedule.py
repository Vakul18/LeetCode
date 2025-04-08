"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


"""
class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x : x[1])
    n = len(jobs)
    dp = [0] * (n+1)
    
    for i, (s,e,p) in enumerate(jobs):
      idx = self.search(jobs, i, s)

      dp[i+1] = max(dp[i], dp[idx] + p)

    return dp[n]

  def search(self, jobs, end, s):
    left,right = 0, end

    while left < right:
      mid = (left +right) >> 1

      if jobs[mid][1] > s:
        right = mid

      else:
        left = mid + 1

    return left


---------------------------------------------------------------------

from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        max_profits = [0]
        max_profit_end_times = [-1]

        sorted_indexes = [index for index in range(len(endTime))]
        sorted_indexes.sort(key = lambda x: endTime[x])

        for curr_index in sorted_indexes:
	        
	        # find the closest job that ends before the current job starts
            prev_index = bisect_right(max_profit_end_times, startTime[curr_index]) - 1

            if  max_profits[prev_index] + profit[curr_index] > max_profits[-1]:
                max_profits.append(max_profits[prev_index] + profit[curr_index])

                # update new end time
                max_profit_end_times.append(endTime[curr_index])
        
        return max_profits[-1]
       



        
    
