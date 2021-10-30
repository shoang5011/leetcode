public class Solution {
    public string LongestPalindrome(string s) {
        if (s.Length == 0)
        {
            return 0; 
        }
        int n = s.Length;
        max_len = 0; 
        for (int i=0; i<n;i++){
            for (int j=0;j<n;j++){
                if (CheckPalindrome(i,j,s))
                {
                    max_len= Math.Max(max_len,j-i-1); 
                }
            }
        }
    }

    public bool CheckPalindrome(int i, int j,string s){
        int n = j-i+1; 
        for (int x=i;x<n/2;i++){
            if (s[i]!=s[n-i-1]){
                return false; 
            }
        }
        return true; 
    }

}