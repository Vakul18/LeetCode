/* https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/ 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
a. Can product exceed int range?
b. Empty string
c. arr having single element

[2,1] -> [1,2]
->	revProd = [1]
	ans[0]	= 1, fwdProd = 2
	ans[1] = 2*2 = 4

[1,4,5,1] -> [20,5,4,20]
->	revProd = [20,5,1]
	ans[0] = 20, fwdProd = 1
	ans[1] = 5, fwd = 4
	ans[2] = 4, fwd = 20
	ans[3] = 20
*/
public class Solution{
	public int[] ProductExceptSelf(int[] nums){

		int[] revProd = new int[nums.Length-1];
		int[] ans = new int[nums.Length];
		int prod = 1;
		for(int i = nums.Length-1; i>0; i--){
			int num = nums[i];
			prod *= num;
			revProd[i-1] = prod;
		}

		int fwProd = 1;
		for(int i = 0 ; i<nums.Length-1; i++){
			ans[i] = fwProd * revProd[i];
			fwProd *= nums[i];
		}

		ans[ans.Length-1] = fwProd;
		return ans;
	}
}
