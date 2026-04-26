class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        res = [i for i in range(N)]
        adjList = [[] for _ in range(N)]
        inDegree = [0] * N
        for u, v in richer:
            adjList[u].append(v)
            inDegree[v] += 1

        queue = deque([i for i, degree in enumerate(inDegree) if degree == 0])

        while queue:
            u = queue.popleft()
            for v in adjList[u]:
                if quiet[res[u]] < quiet[res[v]]:
                    res[v] = res[u]
                
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)

        return res