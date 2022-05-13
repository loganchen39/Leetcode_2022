class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        :\Algo. 1, tweeted binary search, handle the special case of 0- or n-rotations, 
        : for the rest cases the minimum must lie in the 2nd segment. 
        :\This can be part of the solution to problem 33. search in rotated sorted array. 
        :\Some key info, if rotated, all of the elements in the 2nd segment are less than those of 
        : the 1st one. You can determine which segment an element lies in by comparing with nums[0].
        : TC: O(logn), 52.69%
        : SC: O(1), 64.29%
        '''
        
        n = len(nums)
        if nums[0] <= nums[n-1]: # 0 or n rotations
            return nums[0]
        
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if mid==hi or nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
                
                
