# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        :\Algo. 1, binary search, find the left bound, i.e. the 1st one, similar 
        : to "34. Find First and Last Position of Element in Sorted Array", 
        : The BF algo with linear search is not implemented, which has O(n) TC.
        : TC: O(logn), 82.83%
        : SC: O(1), 63.24%
        '''
        
        lo, hi = 1, n
        while lo <= hi:
            mid = int((lo+hi)/2)
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                else:
                    hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
    
    
