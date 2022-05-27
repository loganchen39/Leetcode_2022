class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        :\Algo. 1, backtracking with iteration-loop and recursive DFS to search all permutations, 
        : which is different from combinations. For permutation, each iteration needs to start 
        : from 1 here, not something like i+1, and then check if the current number is already in 
        : the current permutation list. For example, current permutation is [3], then it needs to 
        : start from 1, to get [3, 1, 2] etc. The corresponding BF algo. corresponds to n for-loops, 
        : which results in TC of O(n^n). 
        : TC: O(n^n), 65.13%
        : SC: O(), 22.47%, recursion stack. 
        : The output for case [1,2,3] are as follows.
time= 0 , idx= 0 , perm= []
i= 0 , perm= []
time= 1 , idx= 1 , perm= [1]
i= 0 , perm= [1]
i= 1 , perm= [1]
time= 2 , idx= 2 , perm= [1, 2]
i= 0 , perm= [1, 2]
i= 1 , perm= [1, 2]
i= 2 , perm= [1, 2]
time= 3 , idx= 3 , perm= [1, 2, 3]
idx==n, return from one recursion.
before perm.pop(), perm= [1, 2, 3]
before perm.pop(), perm= [1, 2]
i= 2 , perm= [1]
time= 4 , idx= 2 , perm= [1, 3]
i= 0 , perm= [1, 3]
i= 1 , perm= [1, 3]
time= 5 , idx= 3 , perm= [1, 3, 2]
idx==n, return from one recursion.
before perm.pop(), perm= [1, 3, 2]
i= 2 , perm= [1, 3]
before perm.pop(), perm= [1, 3]
before perm.pop(), perm= [1]
i= 1 , perm= []
time= 6 , idx= 1 , perm= [2]
i= 0 , perm= [2]
time= 7 , idx= 2 , perm= [2, 1]
i= 0 , perm= [2, 1]
i= 1 , perm= [2, 1]
i= 2 , perm= [2, 1]
time= 8 , idx= 3 , perm= [2, 1, 3]
idx==n, return from one recursion.
before perm.pop(), perm= [2, 1, 3]
before perm.pop(), perm= [2, 1]
i= 1 , perm= [2]
i= 2 , perm= [2]
time= 9 , idx= 2 , perm= [2, 3]
i= 0 , perm= [2, 3]
time= 10 , idx= 3 , perm= [2, 3, 1]
idx==n, return from one recursion.
before perm.pop(), perm= [2, 3, 1]
i= 1 , perm= [2, 3]
i= 2 , perm= [2, 3]
before perm.pop(), perm= [2, 3]
before perm.pop(), perm= [2]
i= 2 , perm= []
time= 11 , idx= 1 , perm= [3]
i= 0 , perm= [3]
time= 12 , idx= 2 , perm= [3, 1]
i= 0 , perm= [3, 1]
i= 1 , perm= [3, 1]
time= 13 , idx= 3 , perm= [3, 1, 2]
idx==n, return from one recursion.
before perm.pop(), perm= [3, 1, 2]
i= 2 , perm= [3, 1]
before perm.pop(), perm= [3, 1]
i= 1 , perm= [3]
time= 14 , idx= 2 , perm= [3, 2]
i= 0 , perm= [3, 2]
time= 15 , idx= 3 , perm= [3, 2, 1]
idx==n, return from one recursion.
before perm.pop(), perm= [3, 2, 1]
i= 1 , perm= [3, 2]
i= 2 , perm= [3, 2]
before perm.pop(), perm= [3, 2]
i= 2 , perm= [3]
before perm.pop(), perm= [3]
        '''
        
        results = []
        n = len(nums)
        self.time = 0
        
        def backtrack(perm, idx):
            print('time=', self.time, ', idx=', idx, ', perm=', perm)
            self.time += 1
            if idx == n:
                print('idx==n, return from one recursion.')
                results.append(list(perm))
                return
            
            for i in range(n):
                print('i=', i, ', perm=', perm)
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack(perm, idx+1)
                print('before perm.pop(), perm=', perm)
                perm.pop()
        
        backtrack([], 0)
        return results
    
    
