class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe, L = {}, len(graph)
        
        def dfs(node):
            if not node in safe:
                safe[node] = False
                for neighbor in graph[node]:
                    if not dfs(neighbor): break
                else: safe[node] = True
            return safe[node]
        
        list(map(dfs, range(L)))
        
        return [i for i in range(L) if safe[i]]

    def eventualSafeNodes2(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        print(adj, indegree, q)
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # Delete the edge "node -> neighbor".
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes