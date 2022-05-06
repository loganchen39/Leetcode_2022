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
    
    
class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        :\Algo. 2, Instead of processing each of various cases which is error prone, as 
        : there are several cases you may not think of, or understand correctly in the first 
        : place, here we simply find the start/end indices of the digits, and check if the 
        : s[start-1] is '-', '+', or ' ', anything else will make it an invalid number, and 
        : ignore s[end+1, :] if they exist. 
        :\You can NOT simply use int() to get the int, you need to loop the digits to calculate 
        : the number, and check for the overflow or underflow! Need to rewrite.
        :\Due to overflow/underflow, you can NOT loop from s[end] to s[start] which should be 
        : relatively easier, you need to loop from s[start] to s[end] and clamp at some point when 
        : overflow/underflow occurs.
        : TC: O(n), 41.39%
        : SC: O(1), 31.35%
        '''
        
        isNegative = False
        start, end = -1, -2
        n = len(s)
        i = 0
        digitStarted = False
        res = 0
        
        while i < n:
            if not digitStarted:
                if s[i].isdigit():
                    digitStarted = True
                    start = i
                else:
                    pass
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
        
        for i in range(start-1):
            if s[i] != ' ':
                return 0
            
        if start > 0:
            if s[start-1] == '-':
                isNegative = True
            elif s[start-1] == '+':
                pass
            elif s[start-1] == ' ':
                pass
            else:
                return 0
            
        res = int(s[start:end+1])
        if isNegative:
            res = -res
            if res < -2**31:
                res = -2**31
        else:
            if res > 2**31 - 1:
                res = 2**31 - 1
        
        return res
    
    
class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        :\Algo. 3 Follow the rules as in the Leetcode solution. Here what's different 
        : from Algo. 2 is that you don't process various cases, you only move the index 
        : forward when the string character follow "valid" rules, otherwise it will break 
        : out of the loop, and return the default 0 in case of an invalid number. 
        :\Another key point as mentioned in Algo. 2, you have to process the valid number from 
        : left to right to clamp due to possible overflow/underflow.
        : TC: O(n), 75.49% 
        : SC: O(1), 81.00%
        '''
        
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            else:
                break
        
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            #\One trick here for the "or" condition, if sign==1, no problem; if sign==-1, 
            # then "digit > INT_MAX%10" <=> "digit >= 8", 
            # then if digit==8, it's the INT_MIN value, if digit>8, underflow, still need to return INT_MIN. 
            if result > INT_MAX//10 or (result == INT_MAX//10 and digit > INT_MAX%10):
                return INT_MAX if sign==1 else INT_MIN  # not sign*result
            
            result = 10*result + digit
            i += 1
        
        return sign*result
    
    
