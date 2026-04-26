class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matches = {}                        # Stores matches formed. key = girl, value = boy.
        
        def dfs(boy: int, visited: set) -> bool:
            """A depth first search function to match a boy at index `boy` with potential girls.
            
            DFS will go through all of the boy's options and choose the one that maximizes global
            optimum.
            """
            
            for girl in range(N):
                
                # Rule 1. Only ask that girl if you haven't asked her before already.
                # Rule 2. If you wish to ask a girl that's taken, she will only go with you
                #         if her current partner finds a new girl.
                
                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)
                    
                    if girl not in matches or dfs(matches[girl], visited): 
                        matches[girl] = boy                        
                        return True
                
            return False
            
        for boy in range(M):
            dfs(boy, set())
            
        return len(matches)

from scipy.optimize import linear_sum_assignment
class Solution2:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        """
        max matching with hungarian minimum cost bipartite matching: linear_sum_assignment
        """
        size = max(m,n)
        cost_matrix = [[0]*size for i in range(size)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cost_matrix[i][j] = -1
        
        row_idx, col_idx = linear_sum_assignment(cost_matrix)

        return sum(1 for i,j in zip(row_idx, col_idx) if cost_matrix[i][j]!=0)
        