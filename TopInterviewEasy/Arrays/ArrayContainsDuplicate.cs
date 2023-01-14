/*
Find if arrays contains atleast one duplicate element,
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
*/




public class Solution{
	public bool ContainsDuplicate(int[] nums){
	
		var set = new HashSet<int>();
		foreach(int num in nums){
			if(set.Contains(num))
				return true;
			set.Add(num);
		}
		return false;

	}
}
