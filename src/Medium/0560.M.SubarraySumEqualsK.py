class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        :\1. Algo. 1, DID NOT HAVE A CLUE AT FIRST until see the clue, the key math formula is:
        : subarray_sum[i...j] = sum(0, j) - sum(0, i-1), once you have the accumulated sum array.
        : then 2-loop to calculate and compare subarray_sum and the target k.
        : TC: O(n^2), run 1: 72 / 90 test cases passed, Status: Time Limit Exceeded
        : SC: O(1), without deep copy. 
        : For the BF algo. which uses about n nested loops to calculate subarray sum, don't even think about it.
        '''
      
        n = len(nums)
        res = 0
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        subsum = [0] + nums
        
        for i in range(1, n+1):
            for j in range(i, n+1):
                if subsum[j]-subsum[i-1] == k:
                    res += 1
        
        return res
      
      
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        :\1. Algo. 2, based on the math formula in Algo. 1, we can use the hash table. Be aware of the 
        : special case of nums[0] = k, so we need to initialize the dict with element 0:1. 
        :\REITERATE: the key is the math formula in Algo. 1. Initially I didn't have any clue even if I knew 
        : we need to compute the subarray_sum, didn't know how to use it at all.
        : TC: O(n), 20.82%
        : SC: O(n) for the dict, 75.88%
        '''
            
        n = len(nums)
        res = 0
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        dict_existed_sum = {0:1}
        for i in range(n):
            if nums[i] - k in dict_existed_sum:
                res += dict_existed_sum[nums[i]-k]
            
            if nums[i] not in dict_existed_sum:
                dict_existed_sum[nums[i]] = 1
            else:
                dict_existed_sum[nums[i]] += 1
        
        return res
    
    
