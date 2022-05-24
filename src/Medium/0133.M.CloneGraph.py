"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        :\1. Algo. 1. comment: where is the adjList? No need. BFS with a queue, failed with error 
        : "Node with value 2 was not copied but a reference to the original one." Not sure about 
        : what's contained in the self.neighbors, are they Nodes or integers?
        '''
        
        if not node:
            return []
        
        if not node.neighbors:
            node_cp = Node(node.val)
            return node_cp
        
        d = deque([node])
        set_visited = set()
        while d:
            nd = d.popleft()
            nd_cp = Node(nd.val)
            nd_cp.neighbors = [node for node in nd.neighbors]
            if not set_visited:
                nd_first = nd_cp
            set_visited.add(nd_cp.val)
            for node in nd_cp.neighbors:
                if node.val not in set_visited:
                    d.append(node)
        
        return nd_first
    
    
