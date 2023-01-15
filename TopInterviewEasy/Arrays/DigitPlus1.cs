/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
{9} -> {1,0}
{9,9} -> {1,0,0}
{} -> {}
*/

public class Solution{
	public 	int[] PlusOne(int[] digits){
		if(digits.Length == 0)
			return new int[0];
		
		int index = digits.Length-1;
		int sum = digits[index]+1;
		bool isCarry = sum==10;
		int carry = isCarry ?1:0;
		if(isCarry)
			digits[index] = 0;
		else
			digits[index] = sum;
		index--;
		while(index>=0 && carry==1){
			sum = digits[index]+1;
			isCarry = sum==10;
			carry = isCarry ?1:0;
			if(isCarry)
				digits[index] = 0;
			else
				digits[index] = sum;
			index--;
		}
		
		if(carry==0){
			return digits;
		}
		else{
			var list  = new List<int>(){1};
			list.AddRange(digits);
			return list.ToArray();
		}		
		
	}
}


