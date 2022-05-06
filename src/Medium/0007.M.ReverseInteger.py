class Solution:
    def reverse(self, x: int) -> int:
        '''
        :\Algo. 1, digit by digit, starting from the least significant digit, use remainder 
        : and floor division operation. check overflow/underflow. In solution 1, it uses negative 
        : value to get the remainder, here I converted x to positive first. Be aware -3%10 = 7, 
        : it's different, need to make sure it's ok. 
        : TC: O(1) or O(logx), 97.07%
        : SC: O(1), 97.42%
        '''
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        
        INT_MAX = 2**31 - 1
        
        while x > 0:
            digit = x%10
            x = (x-digit)//10  # not / or it becomes float!
            #\below the "or" condition is not necessary, if result==INT_MAX//10 => 214748364
            # then the original number is 463847412 plus one more digit, which is impossible. 
            if result > INT_MAX//10:  # or (result==INT_MAX//10 and digit > INT_MAX%10):
                return 0
            result = 10*result + digit
        
        return sign*result
    
    
