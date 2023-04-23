/*
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
"babad" -> "bab"
"cbbd" -> 
*/
public class Solution {

    public string LongestPalindrome(string s) {
     int maxPalin = 1;
     int start = 0;
     int end = 0;
     for(int i = 1 ; i<s.Length; i++)
     {
      (int currStart, int currEnd, int len) = MaxPalin(s,i);
      //Console.WriteLine($"{currStart},{currEnd},{len}");
      if(len>maxPalin)
      {
        start = currStart;
        end = currEnd;
        maxPalin = len;
      }
     }
     //Console.WriteLine($"{start},{end}");
     return s.Substring(start,end - start +1);
    }

    private (int,int,int) MaxPalin(string s, int index)
    {
      (int oddPalinStart,int oddPalinEnd, int oddPalinLen) = CheckPalin(index,index,s);
      
      if((index-1)<0 || s[index]!=s[index-1])
      {
        return (oddPalinStart, oddPalinEnd, oddPalinLen);
      }
      //Console.WriteLine("reached even");
      int k = index;
      int l = index-1;
      (int evenPalinStart, int evenPalinEnd, int evenPalinLen) = CheckPalin(k,l,s);

      if(evenPalinLen<oddPalinLen)
      {
        return (oddPalinStart, oddPalinEnd, oddPalinLen);
      }     
      else
        return (evenPalinStart, evenPalinEnd, evenPalinLen);
    }

    private (int,int,int) CheckPalin(int start, int end, string s)
    {
      int palinLen = end-start+1;
      int palinStart = start;
      int palinEnd = end;
      start--;
      end++;
      while(start>=0 && end<s.Length)
      {
        if(s[start]==s[end])
        {
          palinStart = start;
          palinEnd = end;
          start--;
          end++;
          palinLen+=2;
        }
        else
        {
          break;
        }
      }
      return(palinStart,palinEnd,palinLen);
    }
}
//
public class Solution {
    int length =0;
    int start =0;
    public string LongestPalindrome(string s) {
        if(s==null || s.Length<=1)
          return s;
          for(int i=0; i<s.Length; i++)
          {
               ExpandFromMiddle(s,i,i);
               ExpandFromMiddle(s,i,i+1);
          }
          return s.Substring(start,length);
    }
    private void ExpandFromMiddle(string s,int i,int j)
    {
        while(i>=0 && j<s.Length &&s[i]==s[j])
        {
            i--;
            j++;
        }
        if(j-i-1>length)
        {
          length =j-i-1;
          start=i+1;
        }
    }
}