# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        :\Algo. 1 BF recursion with implicit function call stack.
        : TC: O(n), 7.30%, n being the number of nodes, each node is visited exactly once.
        : SC: O(h), 29.62%, h being the maximum height, worst case h=n.
        '''
        
        def paths(pt):
            if not pt:
                return []
            
            str_pt = str(pt.val)
            if pt.left:
                left_paths = paths(pt.left)
                for i in range(len(left_paths)):
                    left_paths[i] = str_pt + '->' + left_paths[i]
            else:
                left_paths = []
                
            if pt.right:
                right_paths = paths(pt.right)
                for i in range(len(right_paths)):
                    right_paths[i] = str_pt + '->' + right_paths[i]
            else:
                right_paths = []
            
            if not pt.left and not pt.right:
                return [str_pt]
            else:
                return left_paths + right_paths
        
            
        return paths(root)
    
    
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        :\Algo. 2 iteration with explicit stack, 
        : TC: O(n), 46.35%, n being the number of nodes, each node is visited exactly once.
        : SC: O(h), 29.60%, h being the maximum height, worst case h=n.
        '''
        
        if not root:
            return []
        
        lst_res = []
        stack = [(root, str(root.val))]
        while stack:
            pt, str_path = stack.pop()
            if pt.left:
                stack.append((pt.left, str_path+'->'+str(pt.left.val)))
            if pt.right:
                stack.append((pt.right, str_path+'->'+str(pt.right.val)))
            if not pt.left and not pt.right:
                lst_res.append(str_path)
        
        return lst_res
    
    
