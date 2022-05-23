# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        :\Algo. 1,  DFS Preorder traversal with recursion, same as problem 102. Binary Tree Level Order Traversal, 
        : first top to bottom, then reverse the result. 
        : TC: O(n), 12.25%, each node gets visited once.
        : SC: O(n), 15.01%, for result levels.
        '''
        
        if not root:
            return []
        
        def helper(node, level):
            if level < len(levels):
                levels[level].append(node.val)
            else:
                levels.append([node.val])
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        levels = []
        helper(root, 0)
        levels.reverse()  # inplace operation. 
        return levels  # or return levels[::-1] for reverse
    
    
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        :\Algo. 2, iteration with BFS traversal using queue or deque.
        : TC: O(n), 94.79%, each node gets visited once.
        : SC: O(n), 48.69%, for result lst_res.
        '''
        from collections import deque
        
        if not root:
            return []
        
        lst_res = []
        next_level = deque([root])
        while next_level:
            curr_level = next_level
            next_level = deque([])
            lst_res.append([])
            for pt in curr_level:
                lst_res[-1].append(pt.val)
                if pt.left:
                    next_level.append(pt.left)
                if pt.right:
                    next_level.append(pt.right)
        
        return lst_res[::-1]
    
    
