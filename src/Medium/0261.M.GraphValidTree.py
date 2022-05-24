class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        :\Algo. 1, BFS traverse using a queue or deque, the conditions for a graph to 
        : be a valid tree are: A. the number of edges is n-1, B. the nodes are all connected, i.e. 
        : the number of connected components of the graph is one. For condition B I used BFS traverse 
        : to set visited flag. 
        : \The initial graph structure i.e. edges is not easy to use for traversal, I converted 
        : it to adjacent list. Note for graph we have adjacent list, adjacent matrix, orthogonal 
        : List for digraph, adjacent multilist for undigraph. 
        : TC: O(n+e), 11.07%
        : SC: O(n+e), 89.61%
        '''
        
        if len(edges) != n-1:
            return False

        adj_list = [[] for i in range(n)]
        # print(adj_list)
        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])
            
        visited = [False]*n
        d = deque([0])
        while d:
            curr_node = d.popleft()
            visited[curr_node] = True
            for i in adj_list[curr_node]:
                if not visited[i]:
                    d.append(i)
        
        if all(visited):
            return True
        else:
            return False
        
        
