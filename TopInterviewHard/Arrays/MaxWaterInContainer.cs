/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

[1] -> 0
[1,2] -> 1
[] -> 0

				 | 
				 | 
			   | |   
[1,2,4,1] -> | | | |
[1,8,5,8,1] -> 2*5 + 3*3)
[1,8,5,8,1] -> 

1-8-5-8-1 = 1*4 = 4
1-8 = 1
1-8-5 = 2
1-8-5-8 = 1
max val starting with 1 = 4

8-8-5-1-1

8-8 : 16

--

1 - 1 = 4
1 - 8 = 3
8 - 1 = 3
8 - 8 = 16

  1  8  5  8  1
1 0  1  2  3  4

8 1  0  

5 2     0

8 3        0

1 4           0
          0 n-1
   1 n-1          0 n-2
2 n-1, 1 n-2   1 n-2, 0 n-3

               0-3
       1-3               0-2
  2-3       1-2     1-2      0-1 
3-3 2-2  2-2 1-1  2-2 1-1  0-0 1-1

0 1 2 3

 4 7 3 7 5 4 -> 15
 0 1 2 3 4 5 :

 0-5 -> 4*5 = 20 : 4
 Discard : 1,5

-------
[] -> 0    
[1] -> 0
[1,2,2,1] -> 3 {0,3}
[5,10,2,10,4] -> 20 {1,3}

*/
public class Solution {
	public int MaxArea(int[] height) {
		int maxArea = 0;
		int left = 0;
		int right = height.Length-1;
		while(left<right){
			int currHeight = Math.Min(height[left], height[right]);
			int area = currHeight*(right-left);
			if(area > maxArea)
			{
				maxArea = area;
			}
			while(left<right && height[left] <= currHeight)
			{
				left++;
			}
			if(left == right)
			{
				break;
			}
			while(right>left && height[right] <= currHeight)
			{
				right--;
			}
		}

		return maxArea;
	}
}



    