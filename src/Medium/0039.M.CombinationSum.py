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
    
    
