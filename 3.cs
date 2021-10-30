public class Solution {
    public static void Main(){
        int res; 
        res = LengthOfLongestSubstring("abcabcbb"); 
        Console.WriteLine(res); 
    }
    public int LengthOfLongestSubstring(string s) {
        int n = s.Length;
        int i = 0; 
        int res = 0; 
        var seen = new Dictionary<char,int>(); 
        for (int j = 0;j<n; j++){
            if (seen.ContainsKey(s[j])){
                i = Math.Max(seen[s[j]],i); 
            }
            res = Math.Max(res,j-i+1); 
            seen[s[j]] = j+1 ; 
        } 
        return res; 
    }

}

