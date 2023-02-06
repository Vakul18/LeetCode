/*
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
- [0,0,0] -> [0,0,0]
- [1,0,0,0,-1] -> [1,0,-1],[0,0,0]
*/
public class Solution{
	public IList<IList<int>> ThreeSum(int[] nums) {
		var result  = new List<IList<int>>();
        	for(int i=0;i<nums.Length;i++){
        		int sum = nums[i];
        		var dict = new Dictionary<int,int>();
        		for(int j=0;j<nums.Length;j++){
        			if(j==i)
        				continue;
        			int target = (-1*sum) - nums[j];
        			if(dict.ContainsKey(target)){
        				result.Add(new List<int>{nums[i],nums[j],target});
        			}
				dict[nums[j]] = j;
        		}
        	}
        	return result;
    }
}
