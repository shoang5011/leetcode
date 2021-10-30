using System;

namespace lc11
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            Solution sol = new Solution();
            int[] inp = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
            Console.WriteLine(sol.MaxArea(inp)); 
        }
    }

    public class Solution
    {
        public int MaxArea(int[] height)
        {
            int n = height.Length;
            int max_area = 0;
            int i = 0;
            int j = n - 1; 
            while( j > i)
            {
                if (height[i] > height[j])
                {
                    max_area = Math.Max(max_area, height[j] * (j - i));
                    j--; 
                }
                else
                {
                    max_area = Math.Max(max_area, height[i] * (j - i));
                    i++; 
                }
            }
            return max_area; 
        }
    }
}
