"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.head = None
        # self.curr = None
        self.prev = None
        
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        :\Algo. 1, iterative Inorder Traversal for binary search tree, to keep it sorted. 
        : Use class member self.head and self.prev to store consistent information. 
        : TC: O(n), 32.68%, n being the number of nodes, each node gets visited once.
        : SC: O(h), 98.35%, worst case h=n, 
        '''
        
        if not root:
            return None
        
        stack = [root]
        while stack:
            pt = stack[-1]
            while pt:
                stack.append(pt.left)
                pt = pt.left
            stack.pop()
            if stack:
                pt = stack.pop()
                if not self.head:
                    self.head = pt
                else:
                    self.prev.right = pt
                pt.left = self.prev
                self.prev = pt
                
                stack.append(pt.right)
        
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
    
    
