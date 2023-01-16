/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
{0,12,3,0,4} -> {12,3,4,0,0}
{1,0} -> {0}
{} -> {}
{0} -> {0}
{1} -> {1}

{0,12,3,0,4}
 | |
 {12,0,3,0,4}
    |  |
    
{12,3,0,0,4}
     |    |
     
{12,3,4,0,0}
          ||
*/

public class Solution{
	public void MoveZeroes(int[] nums){
		int lastNonZeroIndex = -1;
		for(int i =0 ; i< nums.Length ;i++){
			if(nums[i]!=0){
				lastNonZeroIndex++;	
				Swap(nums,i,lastNonZeroIndex);
			}
		}		
	}
	
	public void Swap(int[] nums, int i , int j){
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;	
	}
}


public class Solution{
	public void MoveZeroes(int[] nums){
		int lastNonZeroIndex = -1;
		for(int i =0 ; i< nums.Length ;i++){
			if(nums[i]!=0){
				lastNonZeroIndex++;	
				nums[lastNonZeroIndex] = nums[i];
			}
		}		
		for(int i=(lastNonZeroIndex+1); i<nums.Length;i++){
			nums[i] = 0;
		}
	}
}


