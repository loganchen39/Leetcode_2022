class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        :\1. Algo. 1, Kinda BF, use a sorted array to compare. 
        : TC: O(nxlogn) for sort, 24.33%
        : SC: O(n) for ancillary sort array, 54.67%
        '''
        
        n = len(nums)
        res = 0
        
        nums_sorted = sorted(nums)
        lo, hi = 0, n-1
        
        for i in range(n):
            if nums[i] != nums_sorted[i]:
                lo = i
                break
        else:
            return 0
        
        for i in range(n-1, -1, -1):
            if nums[i] != nums_sorted[i]:
                hi = i
                break
                
        return hi - lo + 1
    
    
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        :\Algo. 2, the idea is similar to find the one value of maximum in an array, here we only 
        : need to find the start index of the subarray, which is determined by the smallest number 
        : that goes from the pattern of larger->smaller within nums[0->n-1]; and the end index of the 
        : subarray, which is determined by largest number that goes from the pattern of smaller->larger 
        : within nums[n-1->0]. 
        : TC: O(n), 29.75%,
        : SC: O(1), 54.67%
        '''
        
        n = len(nums)

        low = -1
        num_low = 1000000
        for i in range(1, n):
            if nums[i] < nums[i-1] and nums[i] < num_low:
                low = i
                num_low = nums[i]
        
        if low == -1:
            return 0
        else:
            for i in range(n):
                if num_low < nums[i]:
                    start = i
                    break
        
        high = n
        num_high = -1000000
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1] and nums[i] > num_high:
                high = i
                num_high = nums[i]
        
        if high == n:
            return 0
        else:
            for i in range(n-1, -1, -1):
                if num_high > nums[i]:
                    end = i
                    break
        
        return end - start + 1
    
    
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        :\Algo. 3, Another BF, 2-loop to check all pairs with descending order to update the left/right boundary. 
        : TC: O(n^2), 208 / 307 test cases passed. Status: Time Limit Exceeded
        : SC: O(1), 
        '''
        
        n = len(nums)
        
        l, r = n, -1
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    l = min(l, i)
                    r = max(r, j)
        
        if l <= r:
            return r-l+1
        else:
            return 0
        
        
