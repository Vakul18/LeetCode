/* https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/833/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

45,2,48,46,1,47,49,47

45-49 : 5
1-2  : 2

[100,4,200,1,3,2]

100 : 1 , 100 : 1
  4 : 1 ,   4 : 1
200 : 1 , 200 : 1
  1 : 1 ,   1 : 1

100 : 1 , 100 : 1
  3 : 2 ,   4 : 2
200 : 1 , 200 : 1
  1 : 1 ,   1 : 1

100 : 1 , 100 : 1         
   ,   4 : 4        
200 : 1 , 200 : 1
  1 : 4 ,   
||

100 : 1 , 100 : 1
  1 : 4 ,   4 : 4
200 : 1 , 200 : 1

*/

public class Solution{
	public int LongestConsecutive(int[] nums){
		//var uniqueSet  = new HashSet<int>();
		var startDict = new Dictionary<int, int>();
		var endDict = new Dictionary<int, int>();

		foreach(int num in nums){
			if(startDict.ContainsKey(num) || endDict.ContainsKey(num)){
				continue;
			}
			else if(startDict.ContainsKey(num+1)){
				int count1 = startDict[num+1];
				
				if(endDict.ContainsKey(num-1))
				{
					int count2 = endDict[num-1];
					int firstNum = num-count2;
					startDict[firstNum] = count1 + count2 + 1;
					int lastNum = num+count1;
					endDict[lastNum] = count1 + count2 + 1;
					startDict.Remove(num+1);
					endDict.Remove(num-1);
				}
				else
				{
					int endDictKey = num+count1;
					endDict[endDictKey] += 1;
					startDict.Remove(num+1);
					startDict[num] = count1+1;
				}
			}
			else if(endDict.ContainsKey(num-1)){
				int count = endDict[num-1];
				int startKey  = num-count;
				endDict.Remove(num-1);
				endDict[num] = count+1;
				startDict[startKey] = count+1;
			}
			else
			{
				startDict[num] = 1;
				endDict[num] = 1;
			}
		}

		int maxLen = 0;
		foreach(int value in startDict.Values){
			maxLen = Math.Max(value, maxLen);
		}
		return maxLen;
	}
}

//

using System.Collections.Generic;

public class Solution {
    public int LongestConsecutive(int[] nums) {
        if(nums is null || nums.Length == 0) return 0;

        // Add nums to hash set
        HashSet<int> set = new HashSet<int>(nums);
        int longestStreak = 0;

        foreach(int num in set){
            // check for previous number and calculate longest streak
            
            if(!set.Contains(num - 1)){

                int currentStreak = 1;
                int currentNumber = num;

                while(set.Contains(currentNumber + 1)){
                    currentStreak += 1;
                    currentNumber += 1;
                }

                longestStreak = Math.Max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}


