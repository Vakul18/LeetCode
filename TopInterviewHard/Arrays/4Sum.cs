/* https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/829/
[...-70] [..10 30 40] [...30..] [..0 20.]

[0 10 20 70]
[0 1 14 30]
[-50 -20 -30 0]
[0 0 0 0]

1. Find negatives of number in other list : nums12, nums13, nums14, nums23, nums24, nums34 - O(n)
count += nums12*nums34 + nums13*nums24 + nums14*nums23 O(1)
	nums12 = 1(0,0), nums13 = 
2. Find negative of sum of list in other list : nums12-34,nums13-24, nums14-23, exclude 0 case. - O(n^2)
count += nums12-34 + nums13-24 + nums14-23

1 .[1,2]
2. [-2,-1]
3. [-1,2]
4. [0,2]
nums12 = 2, nums13 = 1, nums14 = 0, nums23 = 1, nums24 = 1,nums34 = 0 -> 0 + 1 + 0 = "1" ([0,0,0,1])
nums12-34 = [-1:1, 1:1] : [-1:1, 1:1, 2:1, 4:1] -> 1(-1+1)+ 1(1+ -1) = 2 ([0,0,0,1], [1,1,0,0])
nums13-24 = [3:1, 1:1, 4:1] : [-2:1, -1:1, 1:1] -> 1(1 + -1)  = 1 ([1,1,0,0])
nums14-23 = [1:1, 3:1, 2:1, 4:1] : [-3:1, -2:1, 1:1] -> 1(3 + -3) + 1(2 + -2) = 2 ()

12-34 : [-1:1:(0,0), 0:2:(0,1)-(1,0), 1:1(1,1) ] : [-1:1:(0,0), 1:1:(0,1), 2:1:(1,0), 4:1:(1,1)] -> 1(-1,1)-([0,0,0,1]) + 1(1,-1)[1,1,0,0] = 2
13-24 : [0:1:(0,0), 3:1:(0,1), 1:1:(1,0), 4:1:(1,1)] : [-2:1:(0,0), 0:1:(0,1), -1:1:(1,0), 1:1:(1,1)] -> 1(0,0)-[0,0,0,1] + 1(1,-1)[1,1,0,0] = 2
*/

public class Solution{
	public int FourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4){
	var dict1 = new Dictionary<int,int>();
	var dict2 = new Dictionary<int,int>();
	var dict3 = new Dictionary<int,int>();
	var dict4 = new Dictionary<int,int>();

	AddToDict(dict1, nums1);
	AddToDict(dict2, nums2);
	AddToDict(dict3, nums3);
	AddToDict(dict4, nums4);

	var dict12 = CombineDict(dict1,dict2);
	var dict34 = CombineDict(dict3,dict4);

	int nums12_34 =  FetchMatchCount(dict12, dict34);

	return nums12_34;		
	}

	public Dictionary<int,int> CombineDict(Dictionary<int,int> dict1, Dictionary<int,int> dict2){
		var dict = new Dictionary<int,int>();
		foreach(var kvp1 in dict1){
			foreach(var kvp2 in dict2){
				int item = kvp1.Key + kvp2.Key;
				if(dict.ContainsKey(item)){
					dict[item]+= kvp1.Value * kvp2.Value;
				}
				else{
					dict[item] = kvp1.Value * kvp2.Value;	
				}
			}
		}
		return dict;
	}

	public int FetchMatchCount(Dictionary<int,int> dict1, Dictionary<int,int> dict2){
		int num = 0;
		foreach(var kvp in dict1){
			int val = -1*kvp.Key;
			if(dict2.ContainsKey(val)){
				num += kvp.Value * dict2[val];
			}
		}
		return num;
	}

	public void AddToDict(Dictionary<int,int> dict, int[] arr){
		foreach(int i in arr){
			if(dict.ContainsKey(i)){
				dict[i]++;
			}
			else
			{
				dict[i] = 1;
			}
		}

	}
}
