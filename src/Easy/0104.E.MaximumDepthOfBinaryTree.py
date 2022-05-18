# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        :\Algo. 1, BF recursion with recursion stack, straightforward.
        : TC: O(n), n being the total number of nodes, 71.53%
        : SC: O(m), m being the highest height, worst case n, best case O(logn) with complete tree, 24.15%
        '''
        
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
