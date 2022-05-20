# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        :\Algo. 1, find the path to p, q by recording the path to each node using iteration, then compare. 
        : TC: O(n), 5.01%, for function path(r, p), averagely it should traverse n/2 nodes to find, worst case n, best case 1.
        : SC: O(n), 98.51, stack space, averagely should be around n.
        '''
        
        def path(r, p):
            if r.val == p.val:
                return [r]
            
            stack = [(r, [r])] # need to have (), or it's two elements. 
            while stack:
                pt, lst_path = stack.pop()
                if pt.val == p.val:
                    return lst_path
                else:
                    if pt.right:
                        stack.append((pt.right, lst_path+[pt.right]))
                    if pt.left:
                        stack.append((pt.left, lst_path+[pt.left]))
        
        
        lst_path_p = path(root, p)
        lst_path_q = path(root, q)
        pt_res = root
        i = 0
        min_len = min(len(lst_path_p), len(lst_path_q))
        while i < min_len and lst_path_p[i].val == lst_path_q[i].val:
            i += 1
        
        return lst_path_p[i-1]
    
    
class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        :\Algo. 2, recursion with function call stack for DFS, check each current_node if it's the LCA, 
        : by checking "if mid + left + right >= 2:", which corresponds to several cases, i.e. 
        : A. current_node is p or q, then the other from either left or right child;
        : B. current_node is neither p or q, then p and q are from left AND right children;
        : \Here the root node "1" in Approach 1, will not be recognized as LCA as 
        : "mid + left + right=0+1+0=1", so there will be only 1 node that satisfies the LCA condition, 
        : which is the LCA node. So no need to skip or exit the recursion as soon as we found the LCA 
        : node. Be aware "return mid or left or right", for each node it will return either True or False.
        : TC: O(n), 90.67%, 
        : SC: O(n), 30.80%, 
        '''
        
        def recursiveTraversal(current_node):
            if not current_node:  # or self.ans
                return False
            
            mid = current_node == p or current_node == q
            left = recursiveTraversal(current_node.left)
            right = recursiveTraversal(current_node.right)
            
            if mid + left + right >= 2:
                self.ans = current_node
            
            return mid or left or right
        
        
        recursiveTraversal(root)
        return self.ans
    
    
