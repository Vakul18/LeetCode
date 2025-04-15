"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

priority_tasks_no
priority_tasks_wait
"""
import heapq
class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    
    task_count_map = dict()
    for task in tasks:
      task_count_map[task] = task_count_map.get(task, 0) + 1
    pr_tasks_no = []
    pr_tasks_wait = []
    for key,value in task_count_map.items():
      heapq.heappush(pr_tasks_no, (-value, key))

    curr_interval = 0
    while pr_tasks_no or pr_tasks_wait:
      while pr_tasks_wait:
        if pr_tasks_wait[0][0] <= curr_interval:
          (_, no, task) = heapq.heappop(pr_tasks_wait)
          heapq.heappush(pr_tasks_no, (-no, task))
        else:
          break
        
      if pr_tasks_no:
        (pr, task) = heapq.heappop(pr_tasks_no)
        
        if -pr-1 > 0:
          heapq.heappush(pr_tasks_wait, (curr_interval+n+1, -pr-1,task))
      curr_interval += 1

    return curr_interval


------------

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        job_count = defaultdict(int)

        max_count = 0
        max_value = None

        #Go through, get the number of max count and how many values have it
        for task in tasks:
            job_count[task] += 1
            if job_count[task] > max_count:
                max_count = job_count[task]
                max_value = [task]
            elif job_count[task] == max_count:
                max_value.append(task)

        
        return max(len(tasks), (max_count - 1) * (n+1) + len(max_value))
        
      