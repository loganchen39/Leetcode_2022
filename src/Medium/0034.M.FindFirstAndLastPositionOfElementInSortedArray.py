class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        :\Algo. 1, very similar to original binary search, find the 1st target, then check left/right.
        : TC: O(logn), O(n) in worst cases, 82.68%
        : SC: O(1), 93.77%
        '''
        
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = int((lo+hi)/2)
            if target == nums[mid]:
                left = mid-1
                while left >= 0 and nums[left]==target:
                    left -= 1
                left += 1
                
                right = mid+1
                while right<=n-1 and nums[right]==target:
                    right += 1
                right -= 1
            
                return [left, right]
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        
        return [-1, -1]
    
    
