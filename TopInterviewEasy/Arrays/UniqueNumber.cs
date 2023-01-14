/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
[2,2,1] -> 1
*/

public class Solution{
	public int SingleNumber(int[] nums){
		int xor = 0;
		foreach(int num in nums){
			xor = xor^num;
		}
		return xor;
	}
}
