"""

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums): 

        # ### Recursive
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums): 
        #         return 0
        #     if i in memo: 
        #         return memo[i]

        #     money = max(dfs(i+1),dfs(i+2)+nums[i])
        #     memo[i] = money
        #     return money
        # return dfs(0)

        ### DP 
        if not nums: 
            return 0
        
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[n] = 0 
        dp[n-1] = nums[n-1]

        for i in range(n-2,-1,-1): 
            dp[i] = max(dp[i+1],nums[i]+dp[i+2])

        return dp[0]


