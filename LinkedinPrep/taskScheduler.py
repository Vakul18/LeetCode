"""
1. scheduled task is in past? Will throw exception
2. Is the task to be executed regularly or once? once
3. granularity of time? ms

operations
1. throw exception if timestamp is older than now.
2. store task along with timestamp
3. retrieve tasks older than or equal to the current timestamp.
4. execute each task in a separate process. make sure that the child processes stop, when we kill the main process.

DS

t1 t2 t3 t6

t5 -> t1 t2 t3 t6




"""
import heapq	
from abc import ABC, abstractmethod
from typing import Callable, Union
import heapq
import time
from multiprocessing import process, lock, manager

class DelayedScheduler(ABC):
	@abstractmethod
	def schedule(self, time: int, task: Callable[[], None]):
		"""
		Schedules a task to be executed at a specific time.

		Args:
			delay (int): The unix epoch.
			task (Callable[[], None]): The task to be executed, a function that takes no arguments and returns None.
		"""
		raise NotImplementedError("Subclasses must implement this method")

class DelayedSchedulerImpl(DelayedScheduler):
	
	def __init__(self):
		self.tasks = manager.list([(float('inf'), lambda : None)])
		self.lock = manager.lock()
		execute_process = process(self.execute, args = (self.tasks, self.lock))
		execute_process.daemon = True
		execute_process.start()
	
	def schedule(self, time: int, task: Callable[[], None]):
		curr_timestamp = int(time.time())
		if time < curr_timestamp:
			raise PastTimeStampException(time, curr_timestamp)
		heapq.heappush(self.tasks,(time, (time, task)))

	def execute(self, tasks, lock):
		while True:
			with lock:
				min_time_task = tasks[0]
			while(min_time_task and min_time_task[0] < int(time.time())):
				task_process = Process(target = min_time_task[1])
				task_process.daemon = True
				task_process.start()
				with lock:
					heapq.heappop(tasks)
					min_time_task = tasks[0]
				

			time.sleep(min_time_task[0] - int(time.time()))
			
		
			
			


class PastTimeStampException(Exception):
	def __init__(self, timestamp, curr_timestamp):
		super().__init__(f"Value of timestamp {timestamp} is less than the current timestamp {curr_timestamp}")





