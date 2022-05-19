class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        :\1. Algo. 1, BF with accumulated sum array, 
        : TC: O(n^2), 201 / 209 test cases passed, Status: Time Limit Exceeded
        : SC: O(1) except nums, 
        '''
        
        n = len(nums)
        max_res = -10**5
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        nums = [0] + nums
        
        for i in range(n):
            for j in range(i+1, n+1):
                s = nums[j] - nums[i]
                if s > max_res:
                    max_res = s
        
        return max_res
    
    
