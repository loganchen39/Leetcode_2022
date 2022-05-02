class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        :\Algo. 1. use hash table (dict) to find all the pairs. Here the "maximum" may 
        : misleading, the total number of pairs is fixed. Algo. BF using 2-loop not implemented 
        : which has TC O(n^2). 
        : TC: O(n), 7.94%,
        : SC: O(n) (or O(m) m being the number of distinct values), 54.75%,
        '''
        
        n = len(nums)
        res_max = 0
        dict_ht = {}
        
        for i in range(n):
            if k-nums[i] in dict_ht:
                res_max += 1
                dict_ht[k-nums[i]] -= 1
                if dict_ht[k-nums[i]] == 0:
                    dict_ht.pop(k-nums[i])
            else:
                if nums[i] in dict_ht: 
                    dict_ht[nums[i]] += 1
                else:
                    dict_ht[nums[i]] = 1
        
        return res_max
      
      
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        :\Algo. 2, two-pointer with sorted order, 
        : Special case, k=10, nums: 1, 2, 3, ..., 7, 8, 8, 8, 9, once 2 and the last 8 make a pair, 
        : they will be removed, the rest two 8 will not be made pair with the 2 again. 
        : TC: O(nxlogn), 38.85%
        : SC: O(1), 71.30%
        '''
            
        n = len(nums)
        nums.sort()
        res_max = 0
        lo, hi = 0, n-1
        
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < k:
                lo += 1
            elif s > k:
                hi -= 1
            else:
                res_max += 1
                lo += 1
                hi -= 1
        
        return res_max
    
    
