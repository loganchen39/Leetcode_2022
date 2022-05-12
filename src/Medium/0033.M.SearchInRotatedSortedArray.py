class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        :\Algo. 1, similar idea to binary search, for 2 of the 3 cases, check 
        : which segment (1st or 2nd) does the "mid" lie in, then move to the right section. 
        : TC: O(logn), 54.88%
        : SC: O(1), 57.78%
        '''
        
        n = len(nums)
        lo, hi = 0, n-1
        
        while lo <= hi:
            mid = int((lo+hi)/2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]: 
                if nums[mid] >= nums[lo]:
                    if target >= nums[lo]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    hi = mid - 1
            else: # target > nums[mid]
                if nums[mid] >= nums[lo]:
                    lo = mid + 1
                else:
                    if target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        
        return -1
    
    
