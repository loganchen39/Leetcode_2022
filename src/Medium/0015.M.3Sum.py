class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :\Algo. 1.
        : TC: NA, O(n^3)
        : SC: NA, O(n) for res_SET
        :
        :\BF algo., 3-loop, use set of tuple to avoid duplicate triplets.
        : result: 315 / 318 test cases passed. Status: Time Limit Exceeded
        """
        
        n = len(nums)
        if n <= 2: 
            return []
        
        res_set = set()
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res_set.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return list(res_set)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :\Algo. 2.
        : TC: 97.17%, O(n*logn) for sorting, the rest should be O(n).
        : SC: 15.09%, O(n), for sorted list, dicts set_res etc.
        :
        :\optimized algo. 3 cases: 3 zeros easy; 1 zero relatively easy; no zero, then similar to 2sum, can use dict; 
        : two pointers (normally) with sort;
        :\There could be several senarios for duplicates, e.g. [-6, 4, 2] and [-6, 2, 4], [-6, 3, 3], use set 
        : to avoid duplicates with normally O(1) checkup efficiency. Otherwise your code could be very complicated.
        :\Be aware of the case [..., 6, 6, 6, 6, 6, 6, ...]. 
        """
            
        n = len(nums)
        if n <= 2: 
            return []
        
        nums_sorted = sorted(nums)
             
        set_res = set()
        
        dict_neg = {}
        dict_pos = dict()
        numZero = 0
        
        for i in range(n):
            if nums[i] < 0:
                if nums[i] not in dict_neg:
                    dict_neg[nums[i]] = 1
                else: 
                    dict_neg[nums[i]] += 1
            elif nums[i] == 0:
                numZero += 1
            else:
                if nums[i] not in dict_pos:
                    dict_pos[nums[i]] = 1
                else:
                    dict_pos[nums[i]] += 1
        
        if numZero >= 3:  # case: 3 zeros
            set_res.add((0, 0, 0))
        
        if numZero >= 1:  # case: 1 zero
            idx_neg = 0
            idx_pos = n-1
            while nums_sorted[idx_neg] < 0 and nums_sorted[idx_pos] > 0:
                if abs(nums_sorted[idx_neg]) < nums_sorted[idx_pos]:
                    idx_pos -= 1
                elif abs(nums_sorted[idx_neg]) > nums_sorted[idx_pos]:
                    idx_neg += 1
                else:
                    set_res.add((nums_sorted[idx_neg], 0, nums_sorted[idx_pos]))
                    idx_neg += 1
                    idx_pos -= 1
        
        # case: no zero
        idx_neg = 0
        idx_pos = n-1
        while nums_sorted[idx_neg] < 0 and nums_sorted[idx_pos] > 0:
            if abs(nums_sorted[idx_neg]) <= nums_sorted[idx_pos]:
                curr_tgt = nums_sorted[idx_pos]
                for i in range(idx_neg, n):
                    if nums_sorted[i] >= 0: break
                    if -nums_sorted[i] - curr_tgt in dict_neg: 
                        if nums_sorted[i] != -nums_sorted[i] - curr_tgt or dict_neg[nums_sorted[i]] >= 2:
                            set_res.add(tuple(sorted((nums_sorted[i], -nums_sorted[i] - curr_tgt, curr_tgt))))
                idx_pos -= 1
            else:
                curr_tgt = -nums_sorted[idx_neg]
                for i in range(idx_pos, 0, -1):
                    if nums_sorted[i] <= 0: break
                    if curr_tgt - nums_sorted[i] in dict_pos: 
                        if nums_sorted[i] != curr_tgt - nums_sorted[i] or dict_pos[nums_sorted[i]] >= 2:
                            set_res.add(tuple(sorted((-curr_tgt, curr_tgt-nums_sorted[i], nums_sorted[i]))))
                idx_neg += 1
        
        return list(set_res)

    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :\Algo. 3.
        : TC:5.01%, O(n^2), 2-loop, (O(n*logn) for sorting.)
        : SC: 99.22%, O(n), for sorted list, dicts set_res etc.
        :
        :\not to consider 3 zeros or no zeros cases, sorted array, fix one-element, then two pointers with sorted array, 
        : be careful about how to move the two-pointer. 
        """
        n = len(nums)
        if n <= 2: 
            return []
        
        nums_sorted = sorted(nums)   
        set_res = set()
        
        for curr_idx in range(n): 
            twosum_target = -nums_sorted[curr_idx]
            low, high = 0, n-1
            while low < high:
                if low == curr_idx: 
                    low += 1
                    continue
                if high == curr_idx:
                    high -= 1
                    continue
                    
                if nums_sorted[low] + nums_sorted[high] == twosum_target:
                    set_res.add(tuple(sorted([nums_sorted[curr_idx], nums_sorted[low], nums_sorted[high]])))
                    low += 1
                    high -= 1
                elif nums_sorted[low] + nums_sorted[high] < twosum_target:
                    low += 1
                else:
                    high -= 1
        
        return list(set_res)
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :\Algo. 4.
        : TC: 5.01%, O(n^2), 2-loop
        : SC: 23.33%, O(n), for set_res etc.
        : Another run result:
        : 317 / 318 test cases passed.
        : Status: Time Limit Exceeded
        :
        :\not to consider 3 zeros or no zeros cases, not to use sorted order and two-pointer, fix one number, 
        : then use hash table (i.e. dict, set) to solve the two-sum problem. Use set or sorted tuples to avoid 
        : duplicate results.
        """
            
        n = len(nums)
        if n <= 2: 
            return []
        
        set_res = set()
        
        for curr_idx in range(n):
            twosum_target = -nums[curr_idx]
            set_existed = set()
            for i in range(n):
                if i==curr_idx: 
                    continue
                
                if twosum_target - nums[i] not in set_existed:
                    set_existed.add(nums[i])
                else:
                    set_res.add(tuple(sorted([nums[curr_idx], nums[i], twosum_target-nums[i]])))
        
        return list(set_res)
    
    
