class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        :\Algo. 1, Backtracking with iteration and DFS recursion to search all combinations. 
        : The corresponding BF would be n for-loops to iterate all possible combinations, which made this 
        : problem relatively easier as some other backtracking problems may not be conerted to this simple 
        : fixed number of for-loop problem, e.g. problem 39. Combination Sum. 
        : TC: O(), 16.34%
        : SC: O(), 78.13%
        '''
        
        dict_hm = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
             
        def backtrack(comb, k):
            if k == n:  # base cases
                results.append(comb)
                return
            
            for letter in dict_hm[digits[k]]:
                comb += letter
                backtrack(comb, k+1)
                comb = comb[:-1]
        
        
        n = len(digits)
        if n == 0:
            return [] 
        
        results = []
        backtrack('', 0)
        return results
    
    
