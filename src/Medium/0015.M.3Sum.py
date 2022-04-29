class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        : type nums: List[int]
        : rtype: List[List[int]]
        :
        : TC: NA, O(n^3)
        : SC: NA, O(n) for res_SET
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
        : type nums: List[int]
        : rtype: List[List[int]]
        :
        : TC: 97.17%, O(n*logn) for sorting, the rest should be O(n).
        : SC: 15.09%, O(n), for sorted list, dicts set_res etc.
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
