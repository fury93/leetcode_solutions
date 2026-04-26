class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        N = 10**6
        escapeDist = len(blocked) * 2
        blocked = {tuple(block) for block in blocked}
        
        def check(start, end):
            stack = [tuple(start)]
            visited = {tuple(start)}
            
            while stack:
                r, c = stack.pop()
                if [r, c] == end: return True
                
                manhDist = abs(r - start[0]) + abs(c - start[1])
                if manhDist > escapeDist:
                    return True
                
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in blocked and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            return False

        return check(source, target) and check(target, source)

    # DFS recursive
    def isEscapePossible2(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        N = 10**6
        escapeDist = len(blocked) * 2
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        blocked = {(r, c) for r, c in blocked}
        isReachDestination = False

        def dfs(r, c, start, end, visited):
            if [r, c] == end:
                nonlocal isReachDestination
                isReachDestination = True
                return True

            manhDist = abs(r - start[0]) + abs(c - start[1])
            if manhDist > escapeDist:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in blocked and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if(dfs(nr, nc, start, end, visited)):
                        return True
            return False

        if not dfs(*source, source, target, set()): return False
        return isReachDestination or dfs(*target, target, source, set())