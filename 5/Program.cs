using System;

namespace _5
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = "cbbd";
            Solution sol = new Solution();
            Console.WriteLine(sol.LongestPalindrome(s)); 
        }
    }
    public class Solution
    {
        //// Brute Force 
        //public string LongestPalindrome(string s)
        //{
        //    if (s.Length == 0)
        //    {
        //        return "";
        //    }
        //    // Console.WriteLine(s.Substring(0,1)); 
        //    int n = s.Length;
        //    int max_len = 1;
        //    int start = 0;
        //    for (int i = 0; i < n; i++)
        //    {
        //        for (int j = i; j < n; j++)
        //        {
        //            Console.WriteLine(i.ToString() + j.ToString());
        //            Console.WriteLine(s.Substring(i, j - i));
        //            if (CheckPalindrome(i, j, s) && j - i +1 > max_len)
        //            {
        //                start = i;
        //                max_len = j - i +1 ;
        //                Console.WriteLine("-----" + start.ToString() + max_len.ToString());
        //            }
        //        }
        //    }
        //    return s.Substring(start, max_len);
        //}

        //public bool CheckPalindrome(int i, int j, string s)
        //{
        //    int n = j - i +1;
        //    for (int k = 0; k < n / 2; k++)
        //    {
        //        if (s[i + k] != s[j - k])
        //        {
        //            return false;
        //        }
        //    }
        //    return true;
        //}


        // DP 
        public string LongestPalindrome(string s)
        {
            int n = s.Length;
            bool[,] dp = new bool[n, n];
            int max_len = 1;
            int start = 0; 

            for (int i = 0; i < n; i++)
            {
                dp[i, i] = true; 
            }

            for (int i=0;i < n-1; i++)
            {
                if (s[i] == s[i + 1])
                {
                    start = i; 
                    dp[i,i+1] = true;
                    max_len = 2; 
                }
            }

            for (int k = 3; k <= n; k++)
            {
                for (int i = 0; i < n - k + 1; i++)
                {
                    int j = i + k - 1;
                    //Console.WriteLine(s.Substring(i, k)); 

                    if (dp[i + 1,j-1] && s[i] == s[j])
                    {
                        //Console.WriteLine("------"); 
                        dp[i, j] = true; 
                        if (k > max_len)
                        {
                            start = i; 
                            max_len = k; 
                        } 
                    }
                }
            }

            return s.Substring(start, max_len); 
        }
    }
}

