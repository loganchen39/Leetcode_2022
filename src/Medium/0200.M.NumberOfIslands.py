class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        :\1. Algo. 1, Iterative BFS traversal using queue, and a set to record whether a 
        : node (i, j) has been visited before.
        : TC: O(mxn), 26.80%, 
        : SC: O(mxn), 29.91%, worst case for the queue, e.g. all '1', 
        '''
        
        def BFSTraversal(grid, i, j, visited):
            m, n = len(grid), len(grid[0])
            q = deque([(i, j)])
            while q:
                (k, l) = q.popleft()
                if l+1 < n and grid[k][l+1] == '1' and (k, l+1) not in visited:
                    visited.add((k, l+1))
                    q.append((k, l+1))
                if l-1 >= 0 and grid[k][l-1] == '1' and (k, l-1) not in visited:
                    visited.add((k, l-1))
                    q.append((k, l-1))
                if k+1 < m and grid[k+1][l] == '1' and (k+1, l) not in visited:
                    visited.add((k+1, l))
                    q.append((k+1, l))
                if k-1 >= 0 and grid[k-1][l] == '1' and (k-1, l) not in visited:
                    visited.add((k-1, l))
                    q.append((k-1, l))
                    
                    
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if (i,j) in visited:
                        continue
                    res += 1
                    BFSTraversal(grid, i, j, visited)
        
        return res
      
      
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        :\Algo. 2, recursive DFS traversal, use a set visited to record all the 
        : nodes (i, j) that have been visited.
        : TC: O(mxn), 59.79%, 2-loop, 
        : SC: O(mxn), 26.28%, worst case for the function call stack, e.g. all '1', 
        '''
        
        def DFSTraversal(grid, i, j, visited):
            m, n = len(grid), len(grid[0])
            visited.add((i, j))
            if j+1 < n and grid[i][j+1] == '1' and (i, j+1) not in visited:
                DFSTraversal(grid, i, j+1, visited)
            if j-1 >= 0 and grid[i][j-1] == '1' and (i, j-1) not in visited:
                DFSTraversal(grid, i, j-1, visited)
            if i+1 < m and grid[i+1][j] == '1' and (i+1, j) not in visited:
                DFSTraversal(grid, i+1, j, visited)
            if i-1 >= 0 and grid[i-1][j] == '1' and (i-1, j) not in visited:
                DFSTraversal(grid, i-1, j, visited)
                    
                    
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if (i,j) in visited:
                        continue
                    res += 1
                    DFSTraversal(grid, i, j, visited)
        
        return res  

    
