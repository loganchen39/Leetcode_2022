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
    
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        :\Algo. 2, inspired from approach 1, use binary search to find the pivot index, 
        : the key information here is that, a) all elements are unique, b), you can determine 
        : which segment an element lie in (the 1st or 2nd) by comparing with the nums[0], c) pay 
        : attention to the special cases of pivot at 0, i.e. normal increasing array without pivot.
        : TC: O(logn), 61.90%
        : SC: O(1), 57.78%
        '''
        
        def find_pivot_index(left, right):
            if left == right:
                return left
            
            if nums[left] <= nums[right]:
                return left
            
            while left <= right:
                pivot = (left+right) // 2
                if nums[pivot] > nums[pivot+1]:
                    return pivot+1
                else:
                    if nums[pivot] >= nums[left]:
                        left = pivot + 1
                    else:
                        right = pivot - 1
        
        
        n = len(nums)
        
        pivot = find_pivot_index(0, n-1)
        if target >= nums[0]:
            lo = 0
            if pivot == 0:  # special case
                hi = n - 1
            else:
                hi = pivot - 1
        else:
            lo, hi = pivot, n-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
    
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        :\Failed to re-implement Algo. 1, because it's relatively more complicated to 
        : handle all kinds of scenarios. 
        '''
        
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # target > nums[mid]
                if target <= nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
        return -1
    
    
