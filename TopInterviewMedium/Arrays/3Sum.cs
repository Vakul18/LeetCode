/*
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
- [0,0,0] -> [0,0,0]
- [1,0,0,0,-1] -> [1,0,-1],[0,0,0]
- [-1,0,1,2,-1,-4]
	[-1,0,1] | []
- [-1,0,1,2,-1,-4,-2,-3,3,0,4]
*/
public class Solution{
	public IList<IList<int>> ThreeSum(int[] nums) {
		var result  = new List<IList<int>>();
		var set = new HashSet<string>();
		var duplicateSet = new HashSet<int>();
        	for(int i=0;i<nums.Length;i++){
        		if(!duplicateSet.Add(nums[i]))
        			continue;
        		int sum = nums[i];
        		sum = (-1)*sum;
        		var sumElementsList = sum2(sum,nums,i);
				if(sumElementsList.Count == 0)
					continue;
                foreach (var sumValues in sumElementsList)
                {
                	var triplet = new List<int>();
                	bool numAdded = false;
                	for(int j = 0 ;j<2;j++)
					{
						if(nums[i]<sumValues[j] && !numAdded)
						{
							triplet.Add(nums[i]);
							numAdded = true;
						}
						triplet.Add(sumValues[j]);
					}
					if(triplet.Count<3)
						triplet.Add(nums[i]);
					
					string key = string.Join(",",triplet);
					if(!set.Contains(key))
					{
						result.Add(triplet);
						set.Add(key);
					}	
                }
        	}
			//Console.WriteLine(string.Join(";",set));
        	return result;
    }
	
	List<int[]> sum2(int sum, int[] nums, int ignoreIndex)
	{
		var result  = new List<int[]>();
		var set = new HashSet<int>();
		for(int i = 0 ; i<nums.Length; i++)
		{
			if(i==ignoreIndex)
				continue;
			int target = sum - nums[i];
			if(set.Contains(target))
			{
				if(target<nums[i])
					result.Add(new int[]{target,nums[i]});
				else
					result.Add(new int[]{nums[i],target});
			}
			set.Add(nums[i]);
		}
		return result;
	}
}

//2nd approach
// [-1,0,1,2,-1,-4]
// [-4,-1,-1,0,1,2]
public class Solution{
	public IList<IList<int>> ThreeSum(int[] nums) {
		IList<IList<int>> result = new List<IList<int>>();
		if(nums.Length <3)
			return result;

		Array.Sort(nums);
        //Console.WriteLine(string.Join(";",nums));
		int i = 0;
        while(i< nums.Length-2)
		{
			int currentValue = nums[i];
			int target = currentValue*-1;
			int left = i+1;
			int right = nums.Length-1;
            //Console.WriteLine($" start : {i}, {left}, {right}");
			while(left<right)
			{
				int value = nums[left] + nums[right];
                //Console.WriteLine($" value : {value}, {target}");
				if(target<value)
				{
					right--;
				}
				else if(target>value)
				{
					left++;
				}
				else
				{
                    
					int leftValue = nums[left];
					int rightValue = nums[right];
                    //Console.WriteLine($"{currentValue},{leftValue},{rightValue}");
					result.Add(new List<int>{currentValue,leftValue,rightValue});
					while((left<right) && nums[left] == leftValue)
					{
						left++;
					}		
					while((right>left) && nums[right] == rightValue)
					{
						right--;
					}

				}
			}
			while((i<nums.Length-2) && nums[i] == currentValue)
			{
				i++;
			}
		}
		return result;
    }
}













