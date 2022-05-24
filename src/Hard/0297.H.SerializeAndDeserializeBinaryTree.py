# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    :\0. comment: This is more difficult than the BFS/DFS traversal of the binary trees, as you 
    : need to determine the relationship between the "null" nodes in the serialization within the trees, 
    : To establish the mathemaitical (position) mapping relationship.
    :
    :\Algo. 1, Iterative BFS level-order traversal for binary tree, the mathematical mapping 
    : relationship between tree and sequence is not as hard as I thought initially, for function 
    : serialize which is relatively easier, for a not-None node, you just append its left and right 
    : pointers to the queue or deque, no matter if they are None or not. For deserialize function, 
    : you also need a queue or deque to store all not-None node, and a curr_node and curr_pos to record 
    : the current parent and left-or-right position. 
    :\It requires to use str type to store the result, I initially implemented to use list which should be slightly easier.
    : TC: O(n), 15.51%, each node gets visited once,
    : SC: O(n), 83.54%, to store the str-type result and final tree. 
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        str_res = ''
        d = deque([root])
        while d:
            node = d.popleft()
            if node: 
                str_res += str(node.val)+','
                d.append(node.left)
                d.append(node.right)
            else:
                str_res += 'None,'
        
        while str_res[-5:]=='None,':
            str_res = str_res[:-5]
        
        #print(str_res)
        return str_res

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        #print(data)
        data_list = data.split(',')
        if data_list[-1] == '':
            data_list.pop()
        #print(data_list)
        
        curr_node = root = TreeNode(data_list[0])
        d = deque([root])
        curr_pos = 0
        for i in range(1, len(data_list)):
            if data_list[i] != 'None':
                if curr_pos == 0:
                    curr_node.left = TreeNode(data_list[i])
                    d.append(curr_node.left)
                    curr_pos = 1
                else:
                    curr_node.right = TreeNode(data_list[i])
                    d.append(curr_node.right)
                    d.popleft()
                    if d:
                        curr_node = d[0]
                        curr_pos = 0
                    else:
                        return root
            else:  # 'None'
                if curr_pos == 0:
                    curr_pos = 1
                else:
                    d.popleft()
                    curr_node = d[0]
                    curr_pos = 0
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


