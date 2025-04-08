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




h1 : [0,1]
h2 : [5,3,2]

add 1
add 2
add 5
add 3
add 0


1 . insert acc to when num is w.r.t h1[0], h2[0]
2. Check if len(h1) + 1 < len(h2)
3. If above true then balace the heaps
	if len(h1) < len(h2)
		pop one element from h2 and add to h1
	else 
		pop one element from h1 and add to h2


h1 : [-1,-2]
h2 : [3,2]

add 1
find -> 1
add 2
add 3

find -> 2.5

add 2

h1 : [1,2]
h2 : []

add -1
add -2

h1 : [-6, -2]
h2 : [10]

add 6
add 10
add 2
add 6
add 5 
add 0

0 2 5 6 6 10



"""
import heapq

class MedianFinder:
	def __init__(self):
		self.h1 = []
		self.h2 = []
			
	def addNum(self, num: int) -> None:
		if len(self.h1) == 0:
			heapq.heappush(self.h1, -num)
		else:
			if num <= -self.h1[0]:
				heapq.heappush(self.h1, -num)
			else:
				heapq.heappush(self.h2, num)
			self.balanceHeaps()
	
	
	def balanceHeaps(self):
		len_diff = len(self.h1) -  len(self.h2)
		
		if len_diff == 0 or len_diff == 1:
			return
			
		if len_diff < 0:
			num = heapq.heappop(self.h2)
			heapq.heappush(self.h1, -num)
		else:
			num = -heapq.heappop(self.h1)
			heapq.heappush(self.h2, num)
				

        
	def findMedian(self) -> float:
		count = len(self.h1) + len(self.h2)
		if count & 1 == 1:
			return -self.h1[0]
		else:
			return (self.h2[0] + -self.h1[0])/2



class MedianFinder:

    def __init__(self):
        self.smaller = [] # max heap
        self.larger = [] # min heap

    def addNum(self, num: int) -> None:
        """Time complexity: O(logn)"""
        if len(self.smaller) == len(self.larger):
            heapq.heappush(self.smaller, -heapq.heappushpop(self.larger, num))
        else:
            heapq.heappush(self.larger, -heapq.heappushpop(self.smaller, -num))

    def findMedian(self) -> float:
        """Time complexity: O(1)"""
        if not self.smaller:
            return 0
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        return (-self.smaller[0] + self.larger[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
		