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
    
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 2, iteration with stack, much more complicated than preorderTraversal, failed first 
        : with endless while-loop for example 1, the node "3" has been visited first but then when stack.pop() 
        : the node "2", it append the node "3" again, resulting endless while-loop. Chinese Data Structure 
        : book p. 130, seems to be the same.
        '''
        
        if not root: 
            return []
        
        stack, lst_res = [root], []
        pt = root
        while stack:
            pt = stack[-1]
            while pt.left:
                stack.append(pt.left)
                pt = pt.left
            
            pt = stack.pop()
            lst_res.append(pt.val)
            if pt.right:
                stack.append(pt.right)
        
        return lst_res
    
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 3, same idea with Algo. 2, iteration with stack, succeeded, the key 
        : point here is how to decide to execute "while pt: ", we will append the None pointer 
        : from both pt.left and pt.right, if pt.right == None and it's been appended to stack, 
        : then "while pt: " while not execute again repeatedly as indicated in Algo. 2's problem. 
        : it indicates the left child subtree has all been visited, and now it's the root node's 
        : turn to be visited. 
        : TC: O(n), n being the total number of nodes, 72.15%
        : SC: O(m), m being the highest height of the tree, worst case n, 60.54%
        '''
        
        if not root: 
            return []
        
        stack, lst_res = [root], []
        pt = root
        while stack:
            pt = stack[-1]
            while pt:
                stack.append(pt.left)
                pt = pt.left
            
            stack.pop()
            if stack: 
                #\this if statement is a must, or IndexError: pop from empty list, think of the case with one root node
                # and in fact all cases will end up stack being empty after the above stack.pop().
                pt = stack.pop()
                lst_res.append(pt.val)
                # if pt.right is None, then the above "while pt: " will not
                # execute REPEATEDLY as indicated in Algo.2's problem.
                stack.append(pt.right) 
        
        return lst_res
    
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 4, similar idear with Algo. 2, 3, iteration with stack, here only append non-None 
        : pointers to stack, although we use "pt=pt.left" and "pt=pt.right" to eventually assign None 
        : to  pt, which is used to determine if the curr left-child-subtree has all been visited. 
        : TC: O(n), n being the total number of nodes, 90.45%
        : SC: O(m), m being the highest height of the tree, worst case n, 96.97%
        '''
        
        if not root: 
            return []
        
        stack, lst_res = [], []
        pt = root
        while pt or stack:
            if pt:
                stack.append(pt)
                pt = pt.left
            else:
                pt = stack.pop()
                lst_res.append(pt.val)
                pt = pt.right
        
        return lst_res
    
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        :\Algo. 5, same as Algo. 4, iteration with stack, the key point here which is 
        : the same as Algo. 2~4, is that use pt=pt.right=None to determine if we'll execute 
        : "while pt" to repeatedly do stack.append(pt.left). 
        : TC: O(n), n being the total number of nodes, 11.77%
        : SC: O(m), m being the highest height of the tree, worst case n, 13.22% 
        '''
        
        if not root: 
            return []
        
        stack, lst_res = [], []
        pt = root
        while pt or stack:
            while pt:
                stack.append(pt)
                pt = pt.left
                
            pt = stack.pop()
            lst_res.append(pt.val)
            pt = pt.right
        
        return lst_res
    
    
