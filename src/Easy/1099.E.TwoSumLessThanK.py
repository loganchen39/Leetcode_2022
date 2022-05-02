class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        :\1. Algo. 1 BF, 2-loop over all (i, j) cases,
        : TC: O(n^2), 5.15%
        : SC: O(1), 25.44%
        '''
        
        n = len(nums)
        res_max = -1
        for i in range(n):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                if s < k and s > res_max:
                    res_max = s
                
        return res_max
      
      
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        :\Algo. 2, Two-pointer with sorted order for these array of integers for comparision 
        : (equal to or greater than etc.), 
        : TC: O(n*logn) for sort, 92.16%
        : SC: O(1), 25.44%
        '''
        
        n = len(nums)
        res_max = -1
        nums.sort()
        
        lo, hi = 0, n-1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < k: 
                if s > res_max:
                    res_max = s
                lo += 1
            else:
                hi -= 1
        
        return res_max
