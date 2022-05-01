class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        :\Algo. 1, BF, 2 loops, 
        : TC: faster than 25.39%, O(n^2), not efficient.
        : SC: less than 76.69%, O(1)
        '''
        
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                  
                  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        :\Algo. 2, Use hash table (dict, one-pass) for fast check if an element already exists. 
        : TC: faster than 94.05%, O(n).
        : SC: less than 50.17%, O(n).
        :\consider case, target = 2, you have elements 1, 1, 1, 1, in this one-pass algo it should be ok.
        '''
        
        n = len(nums)
        dict_ht = {}
        
        for i in range(n):
            key_diff = target - nums[i]
            if key_diff in dict_ht:
                return [dict_ht[key_diff], i]
            else:
                dict_ht[nums[i]] = i
               
              
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        :\Algo. 3, similar to algo. 2, Use hash table (dict, two-pass). 
        : TC: faster than 88.00%, O(n).
        : SC: less than 50.17%, O(n).
        :\consider case, target = 2, you have elements 1, 1, 1, 1, well it won't happen due to the assumption that
        : you would have exactly one solution. 
        '''
        
        n = len(nums)
        dict_ht = {}
        
        for i in range(n):
            dict_ht[nums[i]] = i
            
        for i in range(n):
            complement = target - nums[i]
            if complement in dict_ht and dict_ht[complement] != i:
                return [i, dict_ht[complement]]
              
              
