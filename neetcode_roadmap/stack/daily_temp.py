"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

[73,74,75,71,69,72,76,73]
                    | 
[(76, 6), (73, 7)]

[1, 1, 4, 2, 1, 1, 0, 0]

"""
class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    st = []
    res = [0] * len(temperatures)
    """
    temperatures = [73,74,75,71,69,72,76,73]
    st = [(74, 1)]
    res = [1, 0, 0, 0, 0, 0, 0, 0]
    idx, temp = 1 , 74
    """
    for idx, temp in enumerate(temperatures):
      while st and (st[-1][0]  < temp):
        st_temp, st_temp_idx = st.pop()
        res[st_temp_idx] = idx - st_temp_idx

      st.append((temp, idx))

    return res
    
    
    
    
        