class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        '''
        :\1. Algo. BF with 2-loop, 
        : TC: O(n^2), 52.87%
        : SC: O(1), 70.36%
        '''
        
        n = len(nums)
        res_cnt = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j]-nums[i]) == k:
                    res_cnt += 1
        
        return res_cnt
    
    
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        '''
        :\Algo. 2, similar to Two Sum, use hash table (dict), except here you have 2 cases to check,
        :\Not sure if two-pointer with sorted order will work, need to check out.
        : TC: O(n), 87.52% 
        : SC: O(m), m being the number of disctinct values of nums, 70.36%
        '''
        n = len(nums)
        res_cnt = 0
        dict_ht = {}
        
        for i in range(n):
            if nums[i]+k in dict_ht:
                res_cnt += dict_ht[nums[i]+k]
            if nums[i]-k in dict_ht:
                res_cnt += dict_ht[nums[i]-k]
            
            if nums[i] not in dict_ht:
                dict_ht[nums[i]] = 1
            else:
                dict_ht[nums[i]] += 1

        return res_cnt
    
    
