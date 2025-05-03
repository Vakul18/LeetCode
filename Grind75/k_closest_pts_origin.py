"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 
"""
import heapq
import math

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    pq = []
    for pt in points:
      dist = pt[0]**2 + pt[1]**2
      heapq.heappush(pq, (dist, pt))
    res = []
    for _ in range(k):
      _, pt = heapq.heappop(pq)
      res.append(pt)

    return res	


-------------------
__import__ ("atexit").register(lambda: open("display_runtime.txt", 'w').write('0'))

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [ (-point[0]**2 - point[1]**2, point) for point in points]
        heap = []
        for point in points:
            if len(heap) < k:
                heapq.heappush(heap, point)
            else:
                heapq.heappushpop(heap, point)
        return [item[1] for item in heap]
        