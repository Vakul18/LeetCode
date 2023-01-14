/* https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
remove duplicates from a sorted Array
{1,2,3,3,3,4,5} -> {1,2,3,4,5}, k = 5
{2,2,2} -> {2} -> 1
{1} -> {1} -> 1
{} -> 0
{1,2,3,4} ->  {1,2,3,4} -> 4
{2,2,3,3,4}
*/

public class Solution{
	public int RemoveDuplicates(int[] nums){
		if(nums.Length==0)
			return 0;
		int index = 1;
		int lastUniqueIndex = 0;
		while(index<nums.Length){
			if(nums[index]!=nums[lastUniqueIndex]){
				lastUniqueIndex++;
				nums[lastUniqueIndex] = nums[index];
			}
			index++;
		}
			
		return (lastUniqueIndex+1);
	}
}



