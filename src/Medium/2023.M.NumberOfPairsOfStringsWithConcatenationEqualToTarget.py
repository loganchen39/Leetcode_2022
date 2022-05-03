class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        '''
        :\1. Algo. 1, BF with 2-loop to check, what's different from Two Sum is here the order of pair matters.
        : TC: O(n^2), 40.57%
        : SC: O(1), 29.72%
        '''
        
        n = len(nums)
        res_cnt = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    res_cnt += 1
                if nums[j]+nums[i] == target:
                    res_cnt += 1
        
        return res_cnt
    
    
