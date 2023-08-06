/*
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/832/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1

3,8,1
l=0, r=3

1-l = 1, 1-r=-2
l=1, r=3

3,8,2,1
l=0, r=3

2-l = 2, 2-r=-1
l=0,r=2

[12,10,9,8,1,2,3,4,5,6,7]
n = 11
B = sum = 67
A = sum of 1st n+1 = (12*13)/2 = 78
A-B = 11

[12,9,8,1,2,3,4,5,6,7]
n = 10
B = sum = 57
A = sum of 1st n+1 = (11*12)/2 = 66
A-B = 9

[12,9,8,1,2,3,4,5,6,7]
12 : 0-12
9 : 0-9
8 : 0-8
1 : 1-8
2 : 2-8
3 : 3-8
4 :
5 :
6 :
7 : 7-8 -> 8-8


12 : 8-12
9 : 9-12
8 :
1 :
2 :
3 :
4 :
5 :
6 :
7 : 9-12

4,5,6,7,8
4 : 0:4
.
.
8 : 0-4

8,7,6,5,4
8 : 0-8
7 : 0-7
6
5
4 : 0-4

[12,9,8,1,2,3,4,5,6,7,14]
l,r 0,0
12 : l,r 0,12
9 : 0,9
8 : 0,8
1 : 1,8
2 : 2,8
3 : 3,8
4 : 4,8
5 : 5,8
6 : 6,8
7 : 8,8
14 : 8,14
--
12 : 8,12
9 : 9,12
8
1
2
3
4
5
6
7
14 : 9,12

[-1,38,54,4,26,5,21,3,35,-1,13,46,-8,6,29,45,59,12,-10,27,58,40,51,43,2,56,43,37,18,-2,57,58,6,50,1,42,-6,-8,16,-1,1,39,55,4,15,23,19,13,45,19,10,2,-1,0,16,42,27,29,49,15,-3]

-10,-8,-8,-6,-3,-2,-1,-1,-1,-1,0,1,1,2,2,3,4,4,5,6,6,10,12,13,13,15,15,16,16,18,19,19,21,23,26,27,27,29,29,35,37,38,39,40,42,42,43,43,45,45,46,49,50,51,54,55,56,57,58,58,59
*/
public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int l = 0;
        int r = 0;
        for(int i =  0 ; i<2 ; i++){
            foreach(int num in nums){
                int gapTol = Math.Abs(num - l);
                int gapTor = Math.Abs(num - r);
                
                if((l == r) && (num > r)){
                    if(gapTol == 1){
                        l = num;
                        r = num;
                    }
                    else
                    {
                        r = num;
                    }            
                }
                else if((num > l) && (num < r)){
                    
                    if(gapTol == 1 && gapTor == 1)
                    {
                        l = r;
                    }
                    else if(gapTol == 1){
                        l = num;
                    }
                    else
                    {
                        r = num;
                    }
                }
            }
        }
        return l+1;
    }
}

/*3,4,-1,1
3,4,1,1
3 : 3,4,5,1
4 : 3,4,5,5
5 : 7,4,5,5
5 : 7,4,5,5
*/
//

public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int n = nums.Length;
        bool found1 = false;
        for(int i = 0 ; i < n ; i++){
            int num = nums[i];
            if(num == 1)
                found1  = true;
            else if(num > n || num < 1){
                nums[i] = 1;
            }
        }

        if(!found1){
            return 1;
        }

        for(int i = 0 ; i < n ; i++){
            int num = nums[i];
            nums[(num-1)%n] += n;
        }        

        for(int i = 0 ; i < n ; i++){
            int num = nums[i];
            if(num<=n)
                return i+1;
        }

        return n+1;

    }
}