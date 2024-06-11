/*https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/838/
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
s = "a", t = "aa" -> ""
s = "a", t = "a" -> "a"
s = "ADOBECODEBANC", t = "ABC" -> "BANC"



"ADOBECODEBANC"
dict : 'A': 1, 'B': 1, 'C' : 1
minWin : 6
result = ADOBEC
tCount = 3
l : 0 , r : 5

ADOBEC

l : 3 , r : 10
BECODEBA

l : 5 , r : 10
CODEBA



*/
public class Solution {
    public string MinWindow(string s, string t) {
        var dictT  = new Dictionary<char, int>();
        var dict  = new Dictionary<char, int>();
        foreach(char c  in t){
            if(dictT.ContainsKey(c))
                dictT[c]++;
            else
            {
                dictT.Add(c, 1);
                dict.Add(c,0);
            }
        }

        int l = 0;
        int r = 0;
        int tCount  = 0;
        int minWinSize = Int32.MaxValue;
        int bestLeft = -1;
        while(l<=r && r < s.Length){
         
         char currChar = s[r];
         
         if(dict.ContainsKey(currChar)){
            dict[currChar]++;
            
            if(dict[currChar] <= dictT[currChar])
                tCount++;
            if(tCount == t.Length){
                int currLen = r-l + 1;
                
                if(currLen < minWinSize){
                    minWinSize = currLen;
                    bestLeft = l;
                    //Console.WriteLine($"found : {result}");
                }
                
                if(dict.ContainsKey(s[l])){
                    dict[s[l]]--;
                    if(dict[s[l]] < dictT[s[l]])
                        tCount--;
                }
                l++;
                while(l<r && !dict.ContainsKey(s[l])){
                    l++;
                }
                dict[currChar]--;
                if(dict[currChar] < dictT[currChar])
                    tCount--;
            }
            else
                r++;
         }
         else{
            r++;
         }      
        
        }

        return bestLeft == -1 ? string.Empty : s.Substring(bestLeft, minWinSize);
    }
}




//

public class Solution {
    public string MinWindow(string s, string t) {
        int[] count = new int[128];
        int required = t.Length;
        int bestLeft = -1;
        int minLength = s.Length + 1;

        foreach (char c in t)
            count[c]++;

        for (int l = 0, r = 0; r < s.Length; ++r) {
            if(--count[s[r]] >= 0){
                required--;
            }
            while(required == 0){
                int currLen = r - l +1;
                if(currLen < minLength){
                    minLength = currLen;
                    bestLeft = l;
                }

                if(++count[s[l++]] > 0){
                    required++;
                }
            }
        }

        return bestLeft == -1 ? "" : s.Substring(bestLeft, minLength);
    }
}


//

public class Solution {
    public Solution() {
        GC.Collect();
    }

    public string MinWindow(string s, string t) {
        Span<char> targetDict = stackalloc char[128];
        Span<char> windowDict = stackalloc char[128];

        int formedTarget = 0;
        for (int i = 0; i < t.Length; i++) {
            var index = t[i];
            targetDict[index]++;
            if (targetDict[index] == 1) formedTarget++;
        }

        int left = 0, right = 0, formed = 0;
        int minStartIndex = 0, windowSize = 0;
        while (right < s.Length) {
            var rightChar = s[right];
            if (++windowDict[rightChar] == targetDict[rightChar]) formed++;

            while (left <= right && formed == formedTarget) {
                var windowLength = right - left + 1;
                if (windowLength < windowSize || windowSize == 0) {
                    minStartIndex = left;
                    windowSize = windowLength;
                }
                var leftChar = s[left];
                if (--windowDict[leftChar] < targetDict[leftChar]) formed--;
                left++;
            }
            right++;
        }

        return windowSize == 0 ? string.Empty : s.Substring(minStartIndex, windowSize);
    }
}

