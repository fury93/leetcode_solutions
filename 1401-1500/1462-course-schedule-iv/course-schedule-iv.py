class Solution:
    # DFS preprocessing
    def checkIfPrerequisite(self, N: int, prerequisites, queries):
        isPrerequisite = [[False] * N for _ in range(N)]
        adjList = [[] for _ in range(N)]
        for u, v in prerequisites:
            adjList[u].append(v)

        def dfs(parent, child):
            for nei in adjList[child]:
                if not isPrerequisite[parent][nei]:
                    isPrerequisite[parent][nei] = True
                    dfs(parent, nei)

        for i in range(N):
            dfs(i, i)

        return [isPrerequisite[u][v] for u, v in queries]

    # Floyd-Warshall with bitmask O(N^3/64)
    def checkIfPrerequisite1(self, N: int, prerequisites, queries):
        rows = [0] * N
        for u, v in prerequisites:
            rows[u] |= (1 << v)

        for k in range(N):
            for i in range(N):
                if (rows[i] >> k) & 1:
                    rows[i] |= rows[k]

        return [bool((rows[u] >> v) & 1) for u, v in queries]

    # Floyd-Warshall O(N^3)
    def checkIfPrerequisite2(
        self,
        N: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        isPrerequisite = [[False] * N for _ in range(N)]

        for u, v in prerequisites:
            isPrerequisite[u][v] = True

        for k in range(N):
            for i in range(N):
                if isPrerequisite[i][k]:
                    for j in range(N):
                        if isPrerequisite[k][j]:
                            isPrerequisite[i][j] = True

        return [isPrerequisite[u][v] for u, v in queries]