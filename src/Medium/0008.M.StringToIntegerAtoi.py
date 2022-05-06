class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        :\1. Algo. 1, failed, scan/loop over the string and process with various cases. 
        : TC: O(n), failed, presented here for ref. Not sure about the conditions initially.
        : SC: O(1), 
        '''
        
        isNegtive = False
        start, end = 0, -1
        n = len(s)
        i = 0
        digitStarted = False
        res = 0
        
        while i < n:
            if not digitStarted:
                if s[i] == ' ':
                    #i += 1
                    pass
                elif s[i] == '+':
                    pass
                elif s[i] == '-':
                    isNegtive = True
                elif not s[i].isdigit():
                    return 0
                elif s[i].isdigit():
                    digitStarted = True
                    start = i
            else:
                if not s[i].isdigit():
                    end = i-1
                    break
            i += 1
        else:
            if not digitStarted:
                return 0
            else:
                end = n-1
        
        res = int(s[start:end+1])
        if isNegtive:
            res = -res
            if res < -2**31:
                res = -2**31
        else:
            if res > 2**31 - 1:
                res = 2**31 - 1
        
        return res
    
    
