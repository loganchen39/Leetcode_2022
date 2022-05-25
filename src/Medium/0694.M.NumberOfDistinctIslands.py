class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        :\Algo. 1, similar to problem 200. Number of islands, except you need to remove the 
        : "duplicate" islands. Iterative BFS traversal of graph with a queue or deque to find 
        : all the islands, recorded as a list of list of two-item tuples. Two islands are the same, 
        : if after sorting the indices (i, j) of their grid points, the component differences are 
        : all the same. 
        : TC: O(mxn+kxk), 714 / 759 test cases passed. Status: Time Limit Exceeded, k being the number of islands.
        : SC: O(n1), n1 being the number of grid points that are land 1.
        '''
        
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()  # record all of the islands in one set
        curr_island = set()
        islands = []  # record a list of sets of islands
        q = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) in visited:
                        continue
                    self.BFSTraversal(grid, i, j, visited, islands)
        return self.removeDuplicateIslands(islands)
    
    
    def BFSTraversal(self, grid, i, j, visited, islands):
        m, n = len(grid), len(grid[0])
        # islands.append(set((i, j)))
        islands.append([])
        dq = deque([(i, j)])
        while dq:
            (k, l) = dq.popleft()
            visited.add((k, l))
            islands[-1].append((k, l))
            
            if l+1 < n and grid[k][l+1] == 1 and (k, l+1) not in visited:
                dq.append((k, l+1))
            if l-1 >= 0 and grid[k][l-1] == 1 and (k, l-1) not in visited:
                dq.append((k, l-1))
            if k+1 < m and grid[k+1][l] == 1 and (k+1, l) not in visited:
                dq.append((k+1, l))
            if k-1 >= 0 and grid[k-1][l] == 1 and (k-1, l) not in visited:
                dq.append((k-1, l))
    
    
    def removeDuplicateIslands(self, islands):
        k = len(islands)
        for i in range(k):
            islands[i].sort(key=itemgetter(0,1))
        
        for i in range(k):
            for j in range(i+1, k):
                if len(islands[i]) != len(islands[j]) or not islands[i] or not islands[j]:
                    continue
                elif len(islands[i]) == 1 and len(islands[j]) == 1:
                    islands[j] = []
                else:
                    diff0 = tuple(x-y for x,y in zip(islands[j][0], islands[i][0]))
                    for l in range(1, len(islands[i])):
                        diff = tuple(x-y for x,y in zip(islands[j][l], islands[i][l]))
                        if diff != diff0:
                            break
                    else:  # not executed if "break" happened
                        islands[j] = []
        
        res = 0
        for i in range(k):
            if islands[i]:
                res += 1
        
        return res
    
    
