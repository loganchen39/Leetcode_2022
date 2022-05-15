# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\1. Algo. 1 recursion, 
        : TC: O(), 52.29%
        : SC: O( ), 13.35%
        '''
        
        def recursiveTraversal(pt, lst_res):
            if not pt: 
                return
            
            recursiveTraversal(pt.left, lst_res)
            lst_res.append(pt.val)
            recursiveTraversal(pt.right, lst_res)
        
        lst_res = []
        recursiveTraversal(root, lst_res)
        return lst_res
    
    
