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
        : TC: O(n), 7.30%, n being the number of nodes.
        : SC: O(h), 29.62%, h being the maximum height.
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
    
    
