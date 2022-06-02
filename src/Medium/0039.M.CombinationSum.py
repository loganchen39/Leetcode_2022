class Solution:
    def __init__(self):
        self.lst_res = []
        self.curr_list = []
        self.target = 0
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        :\comment: failed and couldn't figure out in the first place!
        '''
        
        def dfs(candidates, target):
            print('\n time: ', self.time, ', target: ', target, ', curr_list: ', self.curr_list)
            self.time += 1
            
            if target < 0:
                self.curr_list = []
                return
            elif target == 0:
                self.lst_res.append(self.curr_list)
                self.curr_list = []
                target = self.target
            else:
                for i in range(len(candidates)):
                    self.curr_list.append(candidates[i])
                    dfs(candidates, target-candidates[i])
        
        self.target = target
        dfs(candidates, target)
        return self.lst_res
    
    
class Solution:
    def __init__(self):
        self.lst_res = []
        self.curr_list = []
        #self.target = 0
        self.time = 0
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        :\comment: failed and couldn't figure out in the first place!
        '''
        
        def dfs(candidates, target):
            print('\n time: ', self.time, ', target: ', target, ', curr_list: ', self.curr_list)
            self.time += 1
            
            if self.curr_list and sum(self.curr_list) == target:
                self.lst_res.append(self.curr_list)
                self.curr_list = []
            elif self.curr_list and sum(self.curr_list) > target:
                self.curr_list.pop()
            else:
                for i in range(len(candidates)):
                    self.curr_list.append(candidates[i])
                    dfs(candidates, target)
        

        dfs(candidates, target)
        return self.lst_res
    
    
class Solution:    
    def __init__(self):
        self.time = 0
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        :\0. comment, really difficult to understand, iteration/loop & recursion! Couldn't figure 
        : out in the first place. 
        : \One key point to understand: In each (deep) level of recursion function call, there's a for-loop, 
        : when it finishes and return back to upper-level recursion call, there's still a for-loop needs 
        : to be finished!
        :\Algo. 1, approach 1, backtracking, iteration & recursive DFS to searh all possible combinations and check. 
        : TC: O(?), 75.93%
        : SC: O(?), 58.30%
        : 
        : For test case example 1, below are the output.
time:  0 , remain= 7 , comb= [] , start= 0
i= 0

 time:  1 , remain= 5 , comb= [2] , start= 0
i= 0

 time:  2 , remain= 3 , comb= [2, 2] , start= 0
i= 0

 time:  3 , remain= 1 , comb= [2, 2, 2] , start= 0
i= 0

 time:  4 , remain= -1 , comb= [2, 2, 2, 2] , start= 0
i= 1

 time:  5 , remain= -2 , comb= [2, 2, 2, 3] , start= 1
i= 2

 time:  6 , remain= -5 , comb= [2, 2, 2, 6] , start= 2
i= 3

 time:  7 , remain= -6 , comb= [2, 2, 2, 7] , start= 3
i= 1

 time:  8 , remain= 0 , comb= [2, 2, 3] , start= 1
i= 2

 time:  9 , remain= -3 , comb= [2, 2, 6] , start= 2
i= 3

 time:  10 , remain= -4 , comb= [2, 2, 7] , start= 3
i= 1

 time:  11 , remain= 2 , comb= [2, 3] , start= 1
i= 1

 time:  12 , remain= -1 , comb= [2, 3, 3] , start= 1
i= 2

 time:  13 , remain= -4 , comb= [2, 3, 6] , start= 2
i= 3

 time:  14 , remain= -5 , comb= [2, 3, 7] , start= 3
i= 2

 time:  15 , remain= -1 , comb= [2, 6] , start= 2
i= 3

 time:  16 , remain= -2 , comb= [2, 7] , start= 3
i= 1

 time:  17 , remain= 4 , comb= [3] , start= 1
i= 1

 time:  18 , remain= 1 , comb= [3, 3] , start= 1
i= 1

 time:  19 , remain= -2 , comb= [3, 3, 3] , start= 1
i= 2

 time:  20 , remain= -5 , comb= [3, 3, 6] , start= 2
i= 3

 time:  21 , remain= -6 , comb= [3, 3, 7] , start= 3
i= 2

 time:  22 , remain= -2 , comb= [3, 6] , start= 2
i= 3

 time:  23 , remain= -3 , comb= [3, 7] , start= 3
i= 2

 time:  24 , remain= 1 , comb= [6] , start= 2
i= 2

 time:  25 , remain= -5 , comb= [6, 6] , start= 2
i= 3

 time:  26 , remain= -6 , comb= [6, 7] , start= 3
i= 3

 time:  27 , remain= 0 , comb= [7] , start= 3
        '''
        
        results = []
        
        def backtrack(remain, comb, start):
            print('\n time: ', self.time, ', remain=', remain, ', comb=', comb, ', start=', start)
            self.time += 1
            
            if remain == 0:
                results.append(list(comb))  # the 'list' is necessary, why?
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                print('i=', i)
                comb.append(candidates[i])
                backtrack(remain-candidates[i], comb, i)
                comb.pop()  # backtrack, return to upper level.
        
        backtrack(target, [], 0)
        return results
    
    
