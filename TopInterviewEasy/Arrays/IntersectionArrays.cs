/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
{1,2,3,3,2} {4,2,3,2} -> {2,3,2}
{} {1,2} -> {}
{1.2,3} {4,5,6} -> {}
*/

public class Solution{
	public int[] Intersect(int[] nums1,int[] nums2){
		var intersect = new List<int>();
		if(nums1.Length==0 || nums2.Length==0)
			return intersect.ToArray();	
		var nums1ByCount = new Dictionary<int,int>();
		var nums2ByCount = new Dictionary<int,int>();
		FillDictionary(nums1ByCount,nums1);
		FillDictionary(nums2ByCount,nums2);
		
		foreach(KeyValuePair<int,int> kvp in nums1ByCount){
			if(nums2ByCount.ContainsKey(kvp.Key))
			{
				int minNumCount = Math.Min(nums2ByCount[kvp.Key],kvp.Value);
				for(int i=0; i<minNumCount;i++){
					intersect.Add(kvp.Key);
				}
			}
		}
				
		
		return intersect.ToArray();
	}
	
	public void FillDictionary(Dictionary<int,int> dictionary,int[] nums){
		foreach(int num in nums)
		{
			if(dictionary.ContainsKey(num)){
				dictionary[num] = dictionary[num]+1;
			}	
			else
			{
				dictionary[num] = 1;
			}
		}
	}
	
}


public class Solution{
	public int[] Intersect(int[] nums1,int[] nums2){
		var intersect = new List<int>();
		if(nums1.Length==0 || nums2.Length==0)
			return new int[0];
		
		bool isNums1Bigger = nums1.Length>nums2.Length;
		
		var biggerArray = isNums1Bigger ? nums1 : nums2;
		var smallerArray = isNums1Bigger ? nums2 : nums1;
		
		var dictionary = new Dictionary<int,int>();

		FillDictionary(dictionary,biggerArray);
		
		foreach(int num in smallerArray){
			if(dictionary.ContainsKey(num) && (dictionary[num]>0)){
				dictionary[num]--;
				intersect.Add(num);
			}
		}
				
		
		return intersect.ToArray();
	}
	
	public void FillDictionary(Dictionary<int,int> dictionary,int[] nums){
		foreach(int num in nums)
		{
			if(dictionary.ContainsKey(num)){
				dictionary[num] = dictionary[num]+1;
			}	
			else
			{
				dictionary[num] = 1;
			}
		}
	}
	
}







