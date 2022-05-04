class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        :\1. Algo. 1, BF with 4-loop, use set of tuples to avoid duplicate.
        : TC: O(n^4), 236 / 289 test cases passed. Status: Time Limit Exceeded
        : SC: about O(n) for returning result.
        '''
        
        n = len(nums)
        set_res = set()
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            set_res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
        
        return list(set_res)
    
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        :\2. Algo. 2, FAILED four-pointer, the criterion to move pointers (at smaller step) does not work here, 
        : see a failed case: [-3,-1,0,2,4,5], target=1; my result is [], while it should be [[-3,-1,0,5]]. 
        : Will this so-called of my four-pointer algo. work?
        : TC: O(nxlogn) for sort, 178 / 289 test cases passed, Status: Wrong Answer
        : OC: about O(n) to store result. 
        '''
            
        l = len(nums)
        if l < 4:
            return []
        
        nums.sort()
        set_res = set()
        i, j, m, n = 0, 1, l-2, l-1
        while j-i!=1 or m-j!=1 or n-m!=1:
            s = nums[i] + nums[j] + nums[m] + nums[n]
            if s == target:
                set_res.add((nums[i], nums[j], nums[m], nums[n]))
                
                if m-j == 1 and j-i == 1:
                    pass
                elif m-j == 1 and j-i != 1:
                    i += 1
                elif m-j != 1 and j-i == 1:
                    j += 1
                else:
                    if nums[i+1] - nums[i] <= nums[j+1] - nums[j]:
                        i += 1
                    else:
                        j += 1
                
                if m-j == 1 and n-m == 1:
                    pass
                elif m-j == 1 and n-m != 1:
                    n -= 1
                elif m-j != 1 and n-m == 1:
                    m -= 1
                else:
                    if nums[m] - nums[m-1] <= nums[n]-nums[n-1]:
                        m -= 1
                    else:
                        n -= 1
            
            elif s < target:
                if m-j == 1 and j-i == 1:
                    break
                elif m-j == 1 and j-i != 1:
                    i += 1
                elif m-j != 1 and j-i == 1:
                    j += 1
                else:
                    if nums[i+1] - nums[i] <= nums[j+1] - nums[j]:
                        i += 1
                    else:
                        j += 1
            
            else:
                if m-j == 1 and n-m == 1:
                    break
                elif m-j == 1 and n-m != 1:
                    n -= 1
                elif m-j != 1 and n-m == 1:
                    m -= 1
                else:
                    if nums[m] - nums[m-1] <= nums[n]-nums[n-1]:
                        m -= 1
                    else:
                        n -= 1
        
        s = nums[i] + nums[j] + nums[m] + nums[n]
        if s == target:
            set_res.add((nums[i], nums[j], nums[m], nums[n]))
        
        return list(set_res)
    
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        :\Algo 3, kSum becomes k-2 loops and twoSum with two-pointers, using set to avoid dupliates. 
        : TC: O(n^3), 35.86% 
        : SC: O(n) for set_res, 65.02%
        '''
            
        n = len(nums)
        if n < 4:
            return []
        
        set_res = set()
        nums.sort()
        
        for i in range(n):
            for j in range(i+1, n): 
                set_twosumii = self.twoSumII(nums, j+1, target-nums[i]-nums[j])
                for (n1, n2) in set_twosumii:
                    set_res.add((nums[i], nums[j], n1, n2))
        
        return list(set_res)
        
    def twoSumII(self, nums: List[int], start: int, target: int):
        n = len(nums)
        set_res = set()
        lo, hi = start, n-1
        
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == target:
                set_res.add((nums[lo], nums[hi]))
                lo += 1
                hi -= 1
            elif s < target:
                lo += 1
            else:
                hi -= 1
                
        return set_res
    
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        :\Algo. 4, use recursion, move pointers or skip calling function to avoid duplicates 
        : without set, the idea of which is similar to 3Sum. Another key idea similar to 3Sum 
        : is that for each current i (e.g. 10), in order to find the rest (target - nums[i]), 
        : you go find in the nums[i+1, :], NO NEED to start from 0, 1, etc. whose cases have 
        : already been included previously when i=0, 1, etc. 
        : TC: O(n^3), 3=k-2+1, for twoSum you have O(n), 55.60%
        : SC: O(kn)? , 65.02% 
        '''
        
        # defined inside of the function fourSum, thus no self
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            lst_res = []    
            
            if k == 2:  # stop/end condition for recursion
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]: 
                    subset = kSum(nums[i+1:], target-nums[i], k-1)
                    for lst_elem in subset:
                        lst_res.append([nums[i]] + lst_elem)
            
            return lst_res
                
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            lst_res = []
            lo, hi = 0, len(nums)-1
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target: 
                    hi -= 1
                else:
                    lst_res.append([nums[lo], nums[hi]])
                    num_lo = nums[lo]
                    hi -= 1
                    lo += 1
                    while lo < hi and nums[lo] == num_lo:
                        lo += 1
            
            return lst_res
                        
        nums.sort()
        return kSum(nums, target, 4)
    
    
