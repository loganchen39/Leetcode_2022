class Solution:
    def reverse(self, x: int) -> int:
        '''
        :\Algo. 1, digit by digit, starting from the least significant digit, use remainder 
        : and floor division operation. check overflow/underflow. In solution 1, it uses negative 
        : value to get the remainder, here I converted x to positive first. Be aware -3%10 = 7, 
        : it's different, need to make sure it's ok. 
        : TC: O(1) or O(logx), 22.62%
        : SC: O(1), 16.59%
        '''
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while x > 0:
            digit = x%10
            x = (x-digit)//10  # not / or it becomes float!
            if result > INT_MAX//10 or (result==INT_MAX//10 and digit > INT_MAX%10):
                return 0
            result = 10*result + digit
        
        return sign*result
    
    
