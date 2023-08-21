/*
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/834/

7,4,6,6,6,6,5
1,2,3,4,5,6,7

4

*/

class Solution {
    
    public int findDuplicate(int[] nums) {
        // 'low' and 'high' represent the range of values of the target        
        int low = 1, high = nums.length - 1;
        int duplicate = -1;
        
        while (low <= high) {
            int cur = (low + high) / 2;

            // Count how many numbers in 'nums' are less than or equal to 'cur'
            int count = 0;
            for (int num : nums) {
                if (num <= cur)
                    count++;
            }
            
            if (count > cur) {
                duplicate = cur;
                high = cur - 1;
            } else {
                low = cur + 1;
            }
        }
        return duplicate;
    }
}

//

class Solution {
    
    // Find the position of the Most Significant Bit in num    
    int calcMaxBit(int num) {
        int bits = 0;
        while (num > 0) {
            num /= 2;
            bits++;
        }
        return bits;
    }

    // Find the largest number in nums
    int findMaxNum(int[] nums) {
        int max_num = 0;
        for (int i = 0; i < nums.length; i++)
            max_num = Math.max(max_num, nums[i]);
        return max_num;
    }
    
    public int findDuplicate(int[] nums) {
        int duplicate = 0;
        int n = nums.length - 1;
        int max_num = findMaxNum(nums);
        int max_bit = calcMaxBit(max_num);
        
        // Iterate over each bit        
        for (int bit = 0; bit < max_bit; bit++) {
            int mask = (1 << bit);
            int base_count = 0, nums_count = 0;

            for (int i = 0; i <= n; i++) {
                // If bit is set in number (i) then add 1 to base_count                
                if ((i & mask) > 0) {
                    base_count++;
                }
                // If bit is set in nums[i] then add 1 to nums_count
                if ((nums[i] & mask) > 0) {
                    nums_count++;
                }
            }

            // If the current bit is more frequently set in nums than it is in 
            // the range [1, 2, ..., n] then it must also be set in the duplicate number
            if (nums_count > base_count) {
                duplicate |= mask;
            }
        }
        return duplicate;
    }
}

//

class Solution {
    public int findDuplicate(int[] nums) {
        
        // Find the intersection point of the two runners.
        int tortoise = nums[0];
        int hare = nums[0];
        
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);

        // Find the "entrance" to the cycle.
        tortoise = nums[0];
        
        while (tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[hare];
        }

        return hare;
    }
}


//

public class Solution {
    public int FindDuplicate(int[] nums) {
        int totalXor = 0;
        int xorValue = 0;
        int prevXorvalue = 0;
        int repNum = 0;
        
        foreach(int num in nums){
           totalXor = totalXor^num;
        }

        foreach(int num in nums){
           int xorValue = totalXor^num;
           if(xorValue == prevXorValue){
            
           }
        }
        return 0;
    }
}


