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
    
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        :\Algo. 2, similar to Algo. 1, now mofify the "return" criterion to find the left/right bound.
        : TC: O(logn), 83.96%
        : SC: O(1), 51.50%
        '''
            
        left = self.findBound(nums, target, True)
        right = self.findBound(nums, target, False)
        return [left, right]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo<=hi:
            mid = int((lo+hi)/2)
            if nums[mid] == target:
                if isFirst:
                    if mid==0 or nums[mid-1] != target:
                        return mid
                    else:
                        hi = mid-1
                else:
                    if mid==n-1 or nums[mid+1] != target:
                        return mid
                    else:
                        lo = mid+1
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        
        return -1
    
    
