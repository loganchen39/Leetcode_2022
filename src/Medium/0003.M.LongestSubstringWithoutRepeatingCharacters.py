class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :\1. Algo. 1, loop/scan to find the longest substring. Better to use dict for fast 
        : check and get the index, or for each new character you need to search to find. 
        : TC: O(n), 17.83%
        : SC: O(n) for dict, 51.82%
        '''
        
        substr = ''
        dict_ch2idx = dict()
        res = 0
        
        for i in range(len(s)):
            if s[i] not in dict_ch2idx:
                dict_ch2idx[s[i]] = len(substr)
                substr += s[i]
            else:
                if len(substr) > res:
                    res = len(substr)
                    
                substr = substr[dict_ch2idx[s[i]]+1:] + s[i]
                dict_ch2idx = {}    
                for j in range(len(substr)):
                    dict_ch2idx[substr[j]] = j
        else:
            if len(substr) > res: 
                res = len(substr)
        
        return res
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :\Algo. 2, BF with 2-loop to check all possible pairs (start & end), 
        : Note that you can access "s: str" in the function check directly.
        : TC: O(n^3), 986 / 987 test cases passed. Status: Time Limit Exceeded
        : SC: O(n) for the set, 
        '''
        
        def check(start: int, end: int):
            set_existed = set()
            for i in range(start, end+1):
                if s[i] not in set_existed:
                    set_existed.add(s[i])
                else:
                    return False
            return True
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j) and (j-i+1) > res:
                    res = j-i+1
        
        return res
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :\Algo. 3, sliding window with two-pointer left & right, move the two-pointer and record the longest substring. 
        : TC: O(2n)=O(n), 93.67%
        : SC: O(m), m being the number of the longest substring. 51.82%
        '''
        
        n = len(s)
        if n == 0:
            return 0
        
        l, r = 0, 0
        res = 0
        set_existed = set()
        
        for i in range(n):
            if s[i] not in set_existed:
                set_existed.add(s[i])
                r = i
            else:
                if r-l+1 > res:
                    res = r-l+1
                r = i
                while s[l] != s[i]:
                    set_existed.remove(s[l])
                    l += 1
                else:    
                    l += 1
        else:
            if r-l+1 > res:
                res = r-l+1
        
        return res
    
    
