public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // HashTable seen = new HashTable();
        var seen = new Dictionary<int,int>(); 

        for (int i = 0;  i < nums.Length;  i++)
        {
            var diff = target - nums[i]; 
            if(seen.ContainsKey(diff))
            {
                return new int[]{i,seen[diff]}; 
            }
            else{
                seen[nums[i]] = i; 
            }
        } 
        return null; 

    }
}