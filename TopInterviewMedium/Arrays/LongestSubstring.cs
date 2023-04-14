//https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
public class Solution {
    public int LengthOfLongestSubstring(string s) {
 		int maxLen = 0;
 		for(int i = 0 ; i< s.Length; i++)
 		{
 			var set = new HashSet<char>();
 			char startChar = s[i];
 			set.Add(startChar);
 			int len = 1;
 			for(int j = i+1; j<s.Length; j++)
 			{
 				if(!set.Add(s[j]))
 				{
 					break;
 				}
 				len++;
 			}
 			maxLen = Math.Max(len,maxLen);
 		}       
 		return maxLen;
    }
}

//

public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if(s.Length==1)
            return 1;
        int maxLen = 0;
        var posByChar = new Dictionary<char,int>();  
        int startPos = 0;
        for(int i = 0 ; i< s.Length; i++)
        {
            char currChar = s[i];
            if(posByChar.ContainsKey(currChar) && posByChar[currChar]>=startPos)
            {
                maxLen = Math.Max(i - startPos,maxLen);
                startPos = posByChar[currChar]+1;                   
            }       
            posByChar[currChar] = i;    
        }
        
        return Math.Max(maxLen, s.Length - startPos);
    }
}