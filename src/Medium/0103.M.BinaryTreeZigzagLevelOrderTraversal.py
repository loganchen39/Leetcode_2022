# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        :\1. Algo. 1, Iterative BFS lever-order traversal of binary trees with a queue or deque. 
        : A queue for each level, use curr_level = next_level, level by level. Zigzag really 
        : doesn't matter, simply reverse it. 
        : TC: O(n), 5.14%, each node gets visited once.
        : SC: O(n), 58.31%, for final result. 
        '''
        
        if not root:
            return []
        next_level = deque([root])
        next_order = 0  # left-to-right, 1: right-to-left
        lst_res = []
        
        while next_level:
            curr_level = next_level
            curr_order = next_order
            next_level = deque([])
            next_order = (curr_order+1)%2
            
            curr_list = []
            for node in curr_level:
                curr_list.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if curr_order == 1:
                curr_list.reverse()
            
            lst_res.append(curr_list)
        
        return lst_res
    
    
