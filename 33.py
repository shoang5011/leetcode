class Solution:
    def search(self, nums, target):
        
        def binary_search(arr,low,high,target):
            while low <= high: 
                mid = low + (high-low)//2
                if arr[mid] == target: 
                    return mid 
                elif arr[mid] > target: 
                    high = mid - 1
                else: 
                    low = mid+1
            return -1


        def find_rotate_index(nums): 
            low = 0
            high = len(nums)-1
            while low < high: 
                mid = low + (high-low)//2
                if nums[mid] > nums[mid+1]: 
                    return mid+1
                elif nums[mid] > low: 
                    low = mid
                elif nums[mid] < high: 
                    high = mid
            return -1

        # print(rotate_index)
        if target > nums[0] : 
            rotate_index = find_rotate_index(nums)
            return binary_search(nums,0,rotate_index-1,target)
        elif target < nums[-1]: 
            rotate_index = find_rotate_index(nums)
            return binary_search(nums,rotate_index,len(nums)-1,target)
        elif target == nums[0]: 
            return 0
        elif target == nums[-1]: 
            return len(nums)-1
        else: 
            return -1
        

# nums = [4,5,6,7,0,1,2]
# target = 3
nums = [1]
target = 1 

sol = Solution()
print(sol.search(nums,target))
