//https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
//Input: strs = ["eat","tea","tan","ate","nat","bat"]
//Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// tan <-> nat


public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var strDict = new Dictionary<string,IList<string>>();
        IList<IList<string>> result = new List<IList<string>>();
        foreach(var str in strs)       
        {
            string sortedStr = SortStr(str);
            if(strDict.ContainsKey(sortedStr))
            {
                strDict[sortedStr].Add(str);
            }
            else
                strDict[sortedStr] = new List<string>{str};
        }
        
        return strDict.Values.ToList();
        
    }

    private string SortStr(string str)
    {
        const int max_char = 26;
        int[] charFreq = new int[max_char];
        foreach(char c in str)
        {
            int index = c - 'a';
            charFreq[index]++; 
        }
        var charList = new List<char>();
        for(int i = 0 ;i<max_char;i++)
        {
            for(int j = 0 ;j<charFreq[i];j++)
            {
                charList.Add((char)(i + 'a'));
            }
        }
        return new string(charList.ToArray());
    }
}

//

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var result = new Dictionary<string,IList<string>>();
        foreach(string s in strs){
            char[] hash = new char[26];
            foreach(char c in s){
                hash[c-'a']++;
            }
            string key = new string(hash);
            if(!result.ContainsKey(key)){
                result[key] = new List<string>();
            }

            result[key].Add(s);
        }

        return result.Values.ToList();

    }
}