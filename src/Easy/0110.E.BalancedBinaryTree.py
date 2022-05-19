# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        :\1. Algo. 1, BF using problem 104 recursive maxDepth function, 
        : TC: O(n^2) ?, 33.67%, 
        : SC: O(h), 59.85%, worst case h=n; 
        '''
        
        def depth(pt):
            if not pt:
                return 0
            return max(1+depth(pt.left), 1+depth(pt.right))
        
        
        if not root:
            return True
        
        stack = [root]
        while stack:
            pt = stack.pop()
            if abs(depth(pt.left) - depth(pt.right)) > 1:
                return False
            if pt.right:
                stack.append(pt.right)
            if pt.left:
                stack.append(pt.left)
        
        return True
    
    
