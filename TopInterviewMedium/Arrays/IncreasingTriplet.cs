/*
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
[2,3] -> false
[3,2,1] -> false
[1100,1200,4,3,1400,2,1300]
[1,1,1] -> false
*/
public class Solution{
	public bool IncreasingTriplet(int[] nums){
		bool bucket2Found = false;
		bool bucket3Found = false;
		
		int bucket2 = 0;
		int bucket3 = 0;
		int i = nums.Length-1;
		while(i>=0)
		{
			int element = nums[i];
			if(!bucket3Found || bucket3<=element)
			{
				bucket3 = element;
				bucket3Found = true;
			}
			else if(!bucket2Found || bucket2<=element)
			{
				bucket2 = element;
				bucket2Found = true;	
			}
			else
			{
				return true;
			}
			i--;

		}
		return false;
	}
}

\\
public class Solution{
	public bool IncreasingTriplet(int[] nums){

		int bucket2 = int.MinValue;
		int bucket3 = int.MinValue;
		int i = nums.Length-1;
		while(i>=0)
		{
			int element = nums[i];
			if(element == bucket3 || element == bucket2)
			{ 
			  i--;
			  continue;
			}
			if(bucket3<element)
			{
				bucket3 = element;
			}
			else if(bucket2<element)
			{
				bucket2 = element;
			}
			else
			{
				return true;
			}
			i--;
		}
		return false;
	}
}