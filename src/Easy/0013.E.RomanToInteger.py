  class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        :\Algo. 1, use hash table (dict) for mapping, then accumulate, pay attension to the 2-letter 
        : cases which should be dealt first. Use while-loop in stead of for-loop to handle the irregularity. 
        : TC: O(n), actually O(1), 27.82%
        : SC: O(1), 31.81%
        '''
        
        dict_ht = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4
                   , 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        n = len(s)
        res = 0
        i = 0
        while i < n:
            if i+1 < n and s[i:i+2] in dict_ht:
                res += dict_ht[s[i:i+2]]
                i += 2
            else:
                res += dict_ht[s[i]]
                i += 1
        
        return res
    
    
