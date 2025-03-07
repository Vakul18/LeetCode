"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


m1 = 3, m2 = 4
count = 5


dict = {2 : object, }

1,3,2,4
count
h1(max heap) : 1, h2(min heap): 3

add()
1. if both empty or both have same count add to h1
2. elseif h2 empty add to it.
3. if count is odd, add to h2

fetch()
1. if count is odd : fetch from h1
2. if count is even take mean of h1, h2


-- add 1
self.h1 = [1,3]
self.h2 = [2]
self.count = 1

findmeadian - > 2

-- add 1


[1] [3]




"""
import heapq

class MedianFinder:
	def __init__(self):
		self.h1 = []
		self.h2 = []
		self.count = 0
			
        
	def addNum(self, num: int) -> None:
		if self.count == 1:
			heapq.heappush(self.h2, num)
		elif self.count == 0:
			heapq.heappush(self.h1, -num)
		else:
			if num <= -self.h1[0]:
				heapq.heappush(self.h1, -num)
			else:
				
			
		self.count += 1

        
	def findMedian(self) -> float:
		if self.count & 1 == 1:
			return -self.h1[0]
		else:
			return (self.h2[0] + -self.h1[0])/2
		