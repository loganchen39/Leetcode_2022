# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        :\1. Algo. 1, InorderTraversal correponds to binary search tree, during inorder-traversal 
        : the node value should strictly increasing according to the BST definition.
        : TC: O(n), 40.20%, each node gets visited exactly once.
        : SC: O(h), 95.35%, worst case h=n.
        '''
        
        if not root:
            return True
        
        stack = [root]
        curr_val = -2**31-1
        while stack:
            pt = stack[-1]
            while pt:
                stack.append(pt.left)
                pt = pt.left
            stack.pop()
            if stack:  # this check is NECESSARY!
                pt = stack.pop()
                if pt.val <= curr_val:
                    return False
                else:
                    curr_val = pt.val
                stack.append(pt.right)
        
        return True
    
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        :\Algo. 2, recursive inorder traversal, failed due to curr_val not being consistent, 
        : may need to set it as class member. For [1, 1], the output is as follows:
        : pt.val= 1 , curr_val= -2147483649
        : pt.val= 1 , curr_val= 1
        : pt.val= 1 , curr_val= -2147483649
        : pt.val= 1 , curr_val= 1
        : Output: true  # wrong answer.
        '''
        
        def recursiveInorderTraversal(pt, curr_val):
            if not pt:
                return True
            
            if not recursiveInorderTraversal(pt.left, curr_val):
                return False
            
            print('pt.val=', pt.val, ', curr_val=', curr_val)
            if pt.val <= curr_val:
                return False
            else:
                curr_val = pt.val
            print('pt.val=', pt.val, ', curr_val=', curr_val)
            
            if not recursiveInorderTraversal(pt.right, curr_val):
                return False
            
            return True
        
        
        curr_val = -2**31 - 1
        return recursiveInorderTraversal(root, curr_val)
    
    
class Solution:
    def __init__(self):
        self.curr_val = -2**31 - 1
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        :\same as algo. 2, recursive inorder traversal, succeeded by setting self.curr_val as class member, 
        : TC: O(n), 5.08%, each node gets visited exactly once.
        : SC: O(h), 14.49%, worst case h=n.
        '''
        
        def recursiveInorderTraversal(pt):
            if not pt:
                return True
            
            if not recursiveInorderTraversal(pt.left):
                return False
            
            print('pt.val=', pt.val, ', self.curr_val=', self.curr_val)
            if pt.val <= self.curr_val:
                return False
            else:
                self.curr_val = pt.val
            print('pt.val=', pt.val, ', self.curr_val=', self.curr_val)
            
            if not recursiveInorderTraversal(pt.right):
                return False
            
            return True
        
        
