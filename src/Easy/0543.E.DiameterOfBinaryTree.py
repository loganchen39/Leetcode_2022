# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        :\Algo. 1, recursion, failed on Example 1, my output is 4, while the expected is 3, here in recursive 
        : function maxLen(), edges (2,4) and (2,5) are both counted for node 1, which is wrong, need to use 
        : maxDepth() function from problem 104 to avoid this incorrect situation. 
        '''
        
        def maxLen(pt):
            if not pt: 
                return 0
            if not pt.left and not pt.right:
                return 0
            
            if pt.left:
                maxLeft = 1 + maxLen(pt.left)
            else:
                maxLeft = 0
                
            if pt.right:
                maxRight = 1 + maxLen(pt.right)
            else:
                maxRight = 0
            
            return maxLeft + maxRight
        
        
        if not root:
            return 0
        stack, diam = [root], 0
        while stack:
            pt = stack.pop()
            length = maxLen(pt)
            if length > diam:
                diam = length
            if pt.right:
                stack.append(pt.right)
            if pt.left:
                stack.append(pt.left)
        
        return diam
    
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        :\Algo. 2, based on the comments from Algo. 1, use recursive function maxDepth(),
        : TC: O(n^2), 5.00%
        : SC: O(h), 85.01%, worst case O(n), 
        '''
        
        def maxDepth(pt):
            if not pt:
                return 0
            if not pt.left and not pt.right:
                return 1
            
            left_depth = 1+maxDepth(pt.left)
            right_depth = 1+maxDepth(pt.right)
            return max(left_depth, right_depth)
            
        
        if not root:
            return 0
        
        stack, res_diam = [root], 0
        while stack:
            pt = stack.pop()
            if pt.right:
                right_depth = maxDepth(pt.right)
                stack.append(pt.right)
            else:
                right_depth = 0
                
            if pt.left:
                left_depth = maxDepth(pt.left)
                stack.append(pt.left)
            else:
                left_depth = 0
            
            curr_diam = left_depth + right_depth
            if curr_diam > res_diam:
                res_diam = curr_diam
        
        return res_diam
    
    
# Algo. 3, DFS as approach 1 with O(n). later

