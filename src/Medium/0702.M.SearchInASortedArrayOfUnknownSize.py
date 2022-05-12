# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        '''
        :\Algo. 1, find the section by right*=2 until it's out of the array, then 2 scenarios with binary search.
        : TC: O(logn), 27.96%
        : SC: O(1), 96.34%
        '''
        
        left, right = 0, 1
        num_right = reader.get(right)
        while num_right < 10**5 and target > num_right:
            left = right+1
            right *= 2
            num_right = reader.get(right)
        
        if num_right > 10**5: # check last section
            lo, hi = left, right-1
            while lo <= hi:
                mid = int((lo+hi)/2)
                num_right = reader.get(mid)
                if num_right > 10**5:
                    hi = mid-1
                elif num_right == target:
                    return mid
                elif target < num_right:
                    hi = mid-1
                else:
                    lo = mid+1
                    
            return -1
        elif target <= num_right:  # use binary search
            lo, hi = left, right
            while lo <= hi:
                mid = int((lo+hi)/2)
                if reader.get(mid) == target:
                    return mid
                elif target < reader.get(mid):
                    hi = mid-1
                else:
                    lo = mid+1
            
            return -1
        
        
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        '''
        :\Algo. 2, very similar to Algo. 1, but simpler, no need to differentiate as 2 scenarios.
        : TC: O(logn), 80.16%
        : SC: O(1), 64.96%
        '''
            
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        while target > reader.get(right):
            left = right+1
            right *= 2
        
        while left <= right:
            mid = int((left+right)/2)
            if target == reader.get(mid):
                return mid
            elif target < reader.get(mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
    
    
