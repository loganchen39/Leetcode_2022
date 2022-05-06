class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        '''
        :\Algo. 1, Extract each number and compare with the previous one, not using 
        : str.split() function which would make it easier.
        : TC: O(n), 27.58%
        : SC: O(1), 63.29%
        '''
        
        n = len(s)
        prev_num = -1
        
        i = 0
        while i < n: 
            if s[i].isdigit():
                start = i
                end = i+1
                while end < n:
                    if s[end].isdigit():
                        end += 1
                    else:
                        break
                curr_num = int(s[start:end])
                if curr_num <= prev_num:
                    return False
                else:
                    prev_num = curr_num
                
                i = end
            else:
                i += 1 
        
        return True
    
    
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        '''
        :\Algo. 2, use str.split() then str.isdigit(), a lot easier.
        : TC: O(n), 95.29%
        : SC: O(1), 13.04%
        '''
        
        prev_num = -1
        lst_token = s.split()
        for t in lst_token:
            if t.isdigit():
                curr_num = int(t)
                if curr_num <= prev_num:
                    return False
                else:
                    prev_num = curr_num
        
        return True
    
    
