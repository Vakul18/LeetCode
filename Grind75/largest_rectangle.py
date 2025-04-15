"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [1,1,1,2,3,2,3]
                  1 2 3 4 5 6 8  
0
1-0
2-0
.
.
.
                  
"""
[1,1,1,1,1,3]
max = 6
i = 4
st = [1,2]
h = 6
class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    st = []
    n = len(heights)
    maxRect = 0
    for i in range(n+1):
      while st and ((i == n) or heights[i] <= heights[st[-1]]):
        h = heights[st[-1]]
        st.pop()
        width = 0
        if len(st) == 0:
          width = i
        else:
          width = i - st[-1] - 1
        maxRect = max(maxRect, width*h)
      st.append(i)
    return maxRect


--------------
