class Solution:

    ## backtrack 
    # def canJump(self, nums): 
    #     def backtrack(current_index): 
    #         if current_index == len(nums)-1: 
    #             return True 
    #         for i in range(current_index+1,current_index+nums[current_index]+1): 
    #             if backtrack(i): 
    #                 return True 
    #         return False 
    #     return backtrack(0)

    # ## dp 
    # def canJump(self,nums): 
    #     dp = {}
    #     dp[len(nums)-1] = True 
    #     def backtrack(curr):
    #         if curr in dp: 
    #             return dp[curr]
    #         for i in range(curr+1,curr+1+nums[curr]):
    #             if backtrack(i):
    #                 return True 
    #         return False

    #     return backtrack(0)

    ## one time traverse 

    def canJump(self,nums): 
        last_ind = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if  i + nums[i] >= last_ind: 
                last_ind = i 

        return last_ind == 0

        

inp = [0]    
sol = Solution()
print(sol.canJump(inp))
