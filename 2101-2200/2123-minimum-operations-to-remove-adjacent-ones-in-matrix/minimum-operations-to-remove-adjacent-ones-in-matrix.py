class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        def find(i: int) -> int:
            for j in g[i]:
                if j not in vis:
                    vis.add(j)
                    if match[j] == -1 or find(match[j]):
                        match[j] = i
                        return 1
            return 0

        g = defaultdict(list)
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if (i + j) % 2 and v:
                    x = i * n + j
                    if i < m - 1 and grid[i + 1][j]:
                        g[x].append(x + n)
                    if i and grid[i - 1][j]:
                        g[x].append(x - n)
                    if j < n - 1 and grid[i][j + 1]:
                        g[x].append(x + 1)
                    if j and grid[i][j - 1]:
                        g[x].append(x - 1)

        match = [-1] * (m * n)
        ans = 0
        for i in g.keys():
            vis = set()
            ans += find(i)
        return ans
        
class Solution2:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        matching = defaultdict(lambda: None)
        
		# dfs to find any alternating path from (r, c) between the two parties
		# alternating path means included edges are "matching - unmatching - matching" or "unmatching - matching - unmatching".
		# if one alternating path is found, the max matching can be increased by 1.
        def dfs(r, c, visited):
            visited.add((r, c))
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1) or (nr, nc) in visited: continue
                
				# this step is not in typical dfs but required here, otherwise it will get TLE
				# this is because if (nr, nc) node is already in a matching, we need to skip this node to start dfs again from its matching node, instead of starting dfs from (nr, nc) directly.
                visited.add((nr, nc))
                
				# if (nr, nc) is already in a matching, start dfs from its matching node (let's call it Bob)
				# this is to check if Bob can form another matching and give up the current matching with (nr, nc), so (r, c) can match with (nr, nc) 
                if not matching[nr, nc] or dfs(*matching[nr, nc], visited):
                    matching[r, c] = (nr, nc)
                    matching[nr, nc] = (r, c)
                    return True
            return False
        
        max_matching = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: continue
                if (r % 2) == (c % 2) and dfs(r, c, set()):       # only need to start dfs from cells in one party
                    max_matching += 1
        
        return max_matching