# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        :\1. Algo. 1, BFS with queue, append a None for each level as a flag.
        : TC: O(n), 35.18%, each node gets visited once.
        : SC: O(n), 22.11%, for lst_res.
        '''
        import queue
        
        if not root:
            return []
        
        lst_res = []
        lst_curr = []
        q = queue.Queue()
        # q.put(root, None) # wrong!
        q.put(root)
        q.put(None)
        while not q.empty():
            pt = q.get()
            if not pt:
                if not lst_curr:
                    return lst_res
                lst_res.append(lst_curr)
                lst_curr = []
                q.put(None)
            else:
                lst_curr.append(pt.val)
                if pt.left:
                    q.put(pt.left)
                if pt.right:
                    q.put(pt.right)
                    
                    
class Solution:
    def __init__(self):
        self.lst_res = []
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        :\Algo. 2, recursion, with recursive function helper(node, level). 
        : TC: O(n), 60.38%, each node gets visited once.
        : SC: O(n), 18.89%, for self.lst_res, here it's not necessarily to use class member.
        '''
        
        def helper(node, level):
            if not node:
                return
            
            if level < len(self.lst_res):
                self.lst_res[level].append(node.val)
            else:  # should be level == len(self.lst_res)
                self.lst_res.append([node.val])
            helper(node.left, level+1)
            helper(node.right, level+1)
        
        helper(root, 0)
        return self.lst_res
    
    
