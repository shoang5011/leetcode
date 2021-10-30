"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

"""

from types import _T1


class Solution:
    def rob(self, nums):
        if not nums: 
            return 
        if len(nums)==1: 
            return nums[0]
        n = len(nums)

        def dp(nums): 
            # n = len(nums)
            # dp = [0 for _ in range(n+1)]
            # dp[n] = 0
            # dp[n-1] = nums[n-1]
            # for i in range(n-2,-1,-1): 
            #     dp[i] = max(dp[i+1],dp[i+2]+nums[i])
            # return dp[0]
            p1 = 0
            p2 = 0
            for house in nums: 
                tmp = p1
                p1 = max(p2+house,p1)
                p2 = tmp
            return p1 

        return max(dp(nums[:-1]),dp(nums[1:]))

            