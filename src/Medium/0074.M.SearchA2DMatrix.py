class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        :\Algo. 1, binary search on 2D, same idea.
        : TC: O(logmxn), 64.31%
        : SC: O(1), 90.58%
        '''
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1
        while lo <= hi:
            mid = (lo+hi)//2
            r = mid//n
            c = mid%n
            if target == matrix[r][c]: # for 2D list, can not use [r, c] which is actually tuple.
                return True
            elif target < matrix[r][c]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
    
    
