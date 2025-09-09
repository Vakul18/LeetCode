"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4
 
[5, 4, 2, 3, 4]

[11, 1]

[1, 11]

[1, 2, 3]

st = []
max_rect = 0
1 ,2, 3, 1
|

 0  1  2  3  4  5
[2, 1, 5, 6, 2, 3]

max_rect = 2
st [(2,0)]

idx = 1
height = 1
"""
class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    max_rect = 0
    st = []

    for idx, height in enumerate(heights):
      min_prev_idx = idx
      while st and st[-1][0] >= height:
        prev_height, prev_idx = st.pop()
        max_rect = max(max_rect, prev_height*(idx - prev_idx))
        min_prev_idx = prev_idx
        
      st.append((height, min_prev_idx))

    for height,idx in st:
      max_rect = max(max_rect, height*(len(heights)- idx))

    return max_rect



---------------------
[1, 1, 0]

st [-1, 0]
ans = 0

2 - 0 - 1





class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        ans = 0
        stack = [-1]

        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()

        return ans
