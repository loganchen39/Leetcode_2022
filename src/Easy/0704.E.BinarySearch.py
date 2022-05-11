class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        :\Algo. 1, similar to two-pointer, lo, hi, mid indices. Pay attention to the 
        : while condition, "while lo+1<hi:", in special case of "lo+1==hi", then mid 
        : will always be lo, while target can be equal to nums[hi], so it can not be 
        : "while lo<hi:"; another special case is lo==hi when you nums only has 1 element, 
        : or it has only 2 elements.
        : TC: O(logn), 53.93%
        : SC: O(1), 97.88%
        '''
        
        n = len(nums)
        lo, hi = 0, n-1
        while lo+1 < hi:
            mid = int((lo+hi)/2)
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                lo = mid
            else:
                hi = mid
        
        if nums[hi] == target:
            return hi
        elif nums[lo] == target:
            return lo
        
        return -1
    
    
