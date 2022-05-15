# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\1. Algo. 1, BF recursion, define a new recursion function.
        : TC: O(?), 52.30%
        : SC: O(?) stack?, 60.40%
        '''
        
        def recursiveTraversal(pt, lst_res):
            if not pt:
                return
            
            lst_res.append(pt.val)
            recursiveTraversal(pt.left, lst_res)
            recursiveTraversal(pt.right, lst_res)
        
        lst_res = []
        recursiveTraversal(root, lst_res)
        return lst_res
    
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 2, iteration not recursion, failed with wrong order.
        '''
        
        if not root:
            return []
        
        stack_pt = [root]
        lst_res = []
        while stack_pt:
            pt = stack_pt.pop(0)
            lst_res.append(pt.val)
            if pt.left:
                stack_pt.append(pt.left)
            if pt.right:
                stack_pt.append(pt.right)
        
        return lst_res
    
    
