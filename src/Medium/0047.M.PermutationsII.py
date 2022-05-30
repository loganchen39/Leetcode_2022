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
    
    
