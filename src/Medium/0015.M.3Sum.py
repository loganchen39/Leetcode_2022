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


