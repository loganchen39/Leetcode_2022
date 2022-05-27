class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        :\1. Algo. 1, backtracking with iteration (loop) and recursive DFS traversal to 
        : search for all the combinations. Similar to other backtracking problems. It would 
        : be interesting to see the function call stack.
        : TC: O(), 8.02%
        : SC: O(), 49.58%
        '''
        
        results = []
        
        def backtrack(comb, idx, start):
            if idx == k:  # base case
                results.append(list(comb))
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(comb, idx+1, i+1)
                comb.pop()  # backtrack and return to the upper level
        
        backtrack([], 0, 1)
        return results
    
    
