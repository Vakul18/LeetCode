/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
{2,4,1,5,6},2 -> {5,6,2,4,1}
{1,4,2,5,6}

*/

public class Solution{
	public void Rotate(int[] nums,int k){
		int length = nums.Length;
		int replace = 0;
		int index =0;
		int previousElement = nums[index]
		while(replace<=length){
			int newIndex = (index+k)%(length-1);
			int temp = nums[newIndex];
			nums[newIndex] = previousElement;
			previousElement = temp;
			replace++;
		}
		return;
	}
}
