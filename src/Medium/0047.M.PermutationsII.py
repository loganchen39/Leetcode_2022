class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        :\1. Algo. 1, failed, backtracking, use set to avoid duplicate. 
        '''
        
        results = set()
        n = len(nums)
        indices = set()
        
        def backtrack(perm, idx):
            if idx == n:
                results.add(tuple(perm))
                print('clearing indices ...')
                print('idx=', idx)
                print(indices)
                
                indices.clear()  # error is use "indices = set()"
                return
            
            for i in range(n):
                if i in indices:
                    continue
                print('idx=', idx)
                print(indices)
                indices.add(i)
                perm.append(nums[i])
                backtrack(perm, idx+1)
                perm.pop()
        
        
        backtrack([], 0)
        return list(results)
    
    
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        :\Algo. 2, backtracking, here the key point which is also the reason why Algo. 1 failed, 
        : is that we need to find the permutation of the indices i, not the numbers nums[i], 
        : due to possible duplicate numbers in nums, and then use set to avoid duplicate. 
        : TC: O(), 17.13%
        : SC: O(), 22.73%
        '''
        
        results = set()
        n = len(nums)
        
        def backtrack(perm, idx):
            if idx == n:
                results.add(tuple([nums[i] for i in perm]))
                return
            
            for i in range(n):
                if i in perm:
                    continue
                #perm.append(nums[i])
                perm.append(i)
                backtrack(perm, idx+1)
                perm.pop()
        
        
        backtrack([], 0)
        return list(results)
    
    
