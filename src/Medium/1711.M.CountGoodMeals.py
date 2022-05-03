class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        '''
        :\1. Algo. 1, BF, 2-loop to check if the sum of two numbers is power of two. In this case 
        : sorted order may not be helpful. There seems no usable pattern to check if the SUM of two numbers is power of two.
        : TC: O(n^2xlogn), log(n) for checking if power of two. 56 / 70 test cases passed. Status: Time Limit Exceeded
        : SC: O(1), 
        '''
        
        n = len(deliciousness)
        res_cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                s = deliciousness[i] + deliciousness[j]
                if self.isPowerOfTwo(s):
                    res_cnt += 1
                    
        return res_cnt
    
    def isPowerOfTwo(self, s: int)->bool:
        while s >= 1:
            if s==1 or s==2:
                return True
            
            r = s%2
            s = int((s-r)/2)
            if r==1: 
                return False
              
              
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        '''
        :\1. Algo. 2, key point from hint 1, the number of power of two is at most 22 due to 
        : constraints: 2^0, 2^1, ..., 2^21. Then check if the sum equals to one number becomes equals 
        : to one of the 22 numbers. Still uses 2-loop to get the sum.
        : TC: O(n^2), 59 / 70 test cases passed. Status: Time Limit Exceeded
        : SC: O(1), set_pow with 22 numbers. 
        '''
        
        n = len(deliciousness)
        res_cnt = 0
        set_pow = set([2**i for i in range(22)])
        
        for i in range(n):
            for j in range(i+1, n):
                if deliciousness[i] + deliciousness[j] in set_pow:
                    res_cnt += 1
        return res_cnt
      
      
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        '''
        :\Algo. 3, Similar to Two Sum, use hash table, except here we have 22 sums to check. 
        : TC: O(n), 69 / 70 test cases passed. Status: Wrong Answer
        : SC: O(m), m being distinct values in the array, 
        '''
        
        n = len(deliciousness)
        res_cnt = 0
        list_pow = [2**i for i in range(22)]
        dict_ht = {}
        
        for i in range(n):
            for j in range(22):
                complement = list_pow[j] - deliciousness[i]
                if complement in dict_ht:
                    res_cnt += dict_ht[complement]
                
            if deliciousness[i] not in dict_ht:
                dict_ht[deliciousness[i]] = 1
            else:
                dict_ht[deliciousness[i]] += 1
                    
        return res_cnt
      
      
