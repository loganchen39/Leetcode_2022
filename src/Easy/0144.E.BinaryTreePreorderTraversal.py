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
    
    
