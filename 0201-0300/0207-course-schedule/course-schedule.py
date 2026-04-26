class Solution:
    # Approach 1: Topological Sort Using Kahn's Algorithm
    def canFinish2(self, n, prerequisites):
        adj, rank = [[] for _ in range(n)], [0] * n
        
        for child, parent in prerequisites:
            adj[parent].append(child)
            rank[child] += 1

        visited = 0
        q = deque(i for i in range(n) if rank[i] == 0)
        
        while q:
            course = q.popleft()
            visited += 1

            for nextCourse in adj[course]:
                rank[nextCourse] -= 1
                if rank[nextCourse] == 0:
                    q.append(nextCourse)

        return visited == n

     # Approach 2: Depth First Search
    def canFinish(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        for child, parent in prerequisites:
            adj[parent].append(child)

        visited = [False] * n
        stack = set()

        def dfs(i, visited, stack):
            if i in stack: return False
            if visited[i]: return True
            visited[i] = True
            stack.add(i)

            for child in adj[i]:
                if not dfs(child, visited, stack): return False

            stack.remove(i)
            return True


        for i in range(n):
            if not dfs(i, visited, stack): return False

        return True

