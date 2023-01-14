/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
{2,4,1,5,6},2 -> {5,6,2,4,1}
{2,4,2,5,6} 1
{2,4,2,5,1} 6
{2,6,2,5,1} 4
{2,6,2,4,1} 5
{5,6,2,4,1} 2

{-1,-100,3,99} , 2
{-1,-100,-1,-99} -3
{-3,-100,-1,-99} -1

{1,2,3,4,5,6,7,8,9},3
{1,2,3,1,5,6,7,8,9} 4 1
{1,2,3,1,5,6,4,8,9} 7 2
{7,2,3,1,5,6,4,8,9} 1 3

{1},0

{},1

{1},1

{1,2},1
{1,1} 2

{1,2,3,4,5,6},4
{1,2,3,4,1,6} 5
{1,2,5,4,1,6} 3
{3,2,5,4,1,6} 1


{3,2,1,6,5,4} -> {4,5,6,1,2,3}

 -> {4,5,6,1,2,3}

{-1,-100,3,99} , 2



length=100000
k=54944
 
 
{1,2,3,4,5,6,7}

{2,1,7,6,5,4,3}
{3,4,5,6,7,1,2}



{1,2,3,4,5,6,7},3

{3,2,1,7,6,5,4}

{4,5,6,7,1,2,3}
 
*/

public class Solution{
	public void Rotate(int[] nums,int k){
		if(k==0)
			return;
		int length = nums.Length;
		if(length==0)
			return;
		Console.WriteLine($"length= {length}");
		int replace = 0;
		int index =0;
		int previousElement = nums[index];
		int leastCommonMultiple = lcm(length,k);
        int multiple = leastCommonMultiple/k;
        Console.WriteLine($"multiple= {multiple} , lcm = {leastCommonMultiple}");
		while(replace<length){
			int newIndex = (index+k)%(length);
			int temp = nums[newIndex];
			nums[newIndex] = previousElement;
			previousElement = temp;
			replace++;
			if((replace>1) && (replace>=multiple) && (replace%multiple==0)){
				index = (newIndex+1)%length;
				previousElement = nums[index];
			}
			else
				index = newIndex;
		}
		return;
	}
	
	public int lcm(int a,int b){
		int max = Math.Max(a,b);
		int min = Math.Min(a,b);
		return (a/gcd(max,min))*b;
	}
	
	public int gcd(int a,int b)
	{
		if(a==0)
			return b;
		else if(b==0)
			return a;
		return gcd(b,a%b);
	}
}


public class Solution{
	public void Rotate(int[] nums,int k){
		if(k==0)
			return;
		int length = nums.Length;
		if(length<=1)
			return;
	
		 k = k % length;
		 Array.Reverse(nums,0,k+1);
 		 Array.Reverse(nums,k+1,length-k-1);
 		 Array.Reverse(nums,0,length);
	}
}





















