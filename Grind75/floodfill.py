"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
	
"""
class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    og_color = image[sr][sc]
    image[sr][sc] = color
    st = [(sr,sc)]
    m,n = len(image), len(image[0])
      
    while st:
      r,c = st.pop()
      d = [(1,0), (-1,0), (0,1), (0,-1)]

      for dr,dc in d:
        nr, nc = r+dr, c+dc
        if nr>=0 and nr<m and nc>=0 and nc<n and image[nr][nc] != color and image[nr][nc] == og_color:
          image[nr][nc] = color
          st.append((nr,nc))
    return image
        