class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        :\Algo. 1, failed with time limit exceeded, backtracking with iteration and recursive DFS to search  
        : for all combinations and check, similar to other backtracking problems, e.g. problem 39. One difference is 
        : that here the numbers in candidates can be duplicate, so is the results, e.g. for example 1, 
        : my initial output is [[1,2,5],[1,7],[1,6,1],[2,6],[2,1,5],[7,1]], use a set to remove duplication.
        : \test special case, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 27, why it's time limit
        : exceeded. when no "if sum(candidates) < target:"
        : \test special case, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        : 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        : 1,1,1,1,1] 30
        : time limit exceeded, even with "if sum(candidates) < target:".
        '''
        
        if sum(candidates) < target:
            return []
        
        candidates.sort()
        
        n = len(candidates)
        results = set()
        
        def backtrack(remain, comb, start):
            if remain == 0:
                # results.add(tuple(sorted(comb)))
                results.add(tuple(comb))
                return
            elif remain < 0:
                return
            
            for i in range(start, n):
                comb.append(candidates[i])
                backtrack(remain-candidates[i], comb, i+1)
                comb.pop()
            
            
        backtrack(target, [], 0)
        return list(results)
    
    
