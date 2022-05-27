class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        :\Algo. 1, follow Approach 1 for problem 39. Combination Sum, the problem is to search and 
        : find all eligible combinations and check if it is one of the results, by using iteration 
        : and DFS recursion. Be aware of the base cases (i.e. return) for recursion.
        : \At each level of recursion, there is an iteration or loop, e.g. for example 2, when at 
        : recursive level [1, 2], it will loop over [1, 2, 3 ... 9], once it's done, it will return to 
        : the upper level [1]. Here the corresponding BF algo. would be K for-loop to iterate over all 
        : possible combinations. 
        : TC: O(), 41.49%
        : SC: O(), 27.64%
        '''
        
        results = []
        
        def backtrack(remain, kk, comb, start):
            if kk == 0:  # base cases
                if remain == 0:
                    results.append(list(comb))
                    return
                else:
                    return
            
            for i in range(start, 10):
                comb.append(i)
                backtrack(remain-i, kk-1, comb, i+1)
                comb.pop()  # backtrack to upper level after returning from recursion
        
        backtrack(n, k, [], 1)
        return results
    
    
