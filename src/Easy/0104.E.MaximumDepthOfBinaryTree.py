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
    
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        :\Algo. 2, iteration with explicit stack, the key point here is to attach and record the 
        : depth to each node in the stack, i.e. stack = [[root, 1]], then update. 
        : TC: O(n), 40.54%, n being the total number of nodes, 
        : SC: O(m), 81.17%, m being the number of right-child nodes that are temporarily in the stack, 
        : worst case n/2 when each left-child node has both a left and right-child, while each right-child 
        : does not have any child;, best case O(1) when each tree node does not have left and right-child simultaneously.
        '''
        
        if not root:
            return 0
        
        stack = [[root, 1]]
        maxD = 1
        while stack:
            pt, d = stack.pop()
            if pt.right:
                stack.append([pt.right, d+1])
                if d+1 > maxD:
                    maxD = d+1
            if pt.left:
                stack.append([pt.left, d+1])
                if d+1 > maxD:
                    maxD = d+1

        return maxD
    
    
