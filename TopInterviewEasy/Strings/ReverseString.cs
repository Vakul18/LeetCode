/*
[a,b,c] : 
[a,b,c,d] : 

*/

public class Solution {
    public void ReverseString(char[] s) {
        int n = s.Length;
        int end = n/2;
        for(int i = 0 ; i< end; i++){
            char tempChar = s[i];
            s[i] = s[n-i-1];
            s[n-i-1] = tempChar;
        }        
    }
}

//

public class Solution {
    public void ReverseString(char[] s) {
        for (int i = 0; i < s.Length / 2; i++)
        {
            (s[i], s[s.Length - i - 1]) = (s[s.Length - i - 1], s[i]);
        }
    }
}