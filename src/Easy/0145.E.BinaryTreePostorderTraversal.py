# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 1, BF recursion with implicit recursion stack, 
        : TC: O(n), n being the total number of nodes, 5.13%
        : SC: O(m), m being the highest height of the tree, worst case m=n, 62.78%
        '''
        
        def recursiveTraversal(pt, lst_res):
            if not pt:
                return
            
            recursiveTraversal(pt.left, lst_res)
            recursiveTraversal(pt.right, lst_res)
            lst_res.append(pt.val)
        
        lst_res = []
        recursiveTraversal(root, lst_res)
        return lst_res
    
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 2, iteration with stack, failed with endless while-loop because of repeated assignment, 
        : how to set flag or sign? inorder traversal we use stack.append(pt.right=None) as flag.
        :\seems more complicated than inorder traversal, and the process seems to be different.
        '''
        
        if not root:
            return []
        
        stack, lst_res = [root], []
        while stack:
            pt = stack[-1]
            if pt.right:
                stack.append(pt.right)
            if pt.left:
                stack.append(pt.left)
            
            if not pt.right and not pt.left: 
                pt = stack.pop()
                lst_res.append(pt.val)
        
        return lst_res
    
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 3, iteration with stack, succeeded, key points, 
        :\a. stack.append() right first, then left;
        :\b. set up a boolean flag "visited" for each node, if it's been poped and visited, 
        : then all of its children have been visited, it's time to get its value. 
        : TC: O(n), n being the total number of nodes, 17.70%
        : SC: O(m), m being the highest height of the tree, worst case m=n, 97.26%
        '''
        
        if not root:
            return []
        
        stack, lst_res = [[root, False]], []
        while stack:
            pt, visited = stack[-1]
            if not visited: 
                stack[-1][1] = True
                if pt.right:
                    stack.append([pt.right, False])
                if pt.left:
                    stack.append([pt.left, False])
            else:
                pt = stack.pop()[0]
                lst_res.append(pt.val)
            
            if not pt.right and not pt.left: 
                pt = stack.pop()[0]
                lst_res.append(pt.val)
        
        return lst_res
    
    
