/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
-2147483648

*/
public class Solution {
    public int Reverse(int x) {
        int x1 = x;
        int y = 0;
        while(x1 != 0){
            int digit  = Math.Abs(x1 % 10);
            x1 /= 10;

            if((x < 0) && ((y*10L + digit) > 2147483648)){
                y = 0;
                break;
            }
            else if((x > 0) && ((y*10L + digit) > 2147483647)){
                y = 0;
                break;
            }

            y = y*10 + digit;
        }


        if(x < 0){
            return -y;
        }
        return y;
    }
}

//

public class Solution {
    public int Reverse(int x) {
        int x1 = x;
        int y = 0;
        while(x1 != 0){
            int digit  = Math.Abs(x1 % 10);
            x1 /= 10;

            if(x > 0 && y > Int32.MaxValue/10){
                return 0;
            }
            else if(x < 0 && y > -(Int32.MinValue/10)){
                return 0;
            }   

            y = y*10 + digit;
        }


        if(x < 0){
            return -y;
        }
        return y;
    }
}

//

public class Solution {
    public int Reverse(int x) {
        int sign = (x < 0) ? -1 : 1;
        x *= sign;
        int result = 0;
        while (x > 0) {
            if (result > int.MaxValue/10) return 0;
            result = result * 10 + x % 10;
            x /= 10;
        }
        
        return result * sign;
    }
}

