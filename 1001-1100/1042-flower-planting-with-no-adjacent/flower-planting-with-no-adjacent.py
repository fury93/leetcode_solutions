class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [None] * (n)
        adjList = [[] for _ in range(n+1)]
        for u,v in paths:
            adjList[u].append(v)
            adjList[v].append(u)
        colors = {1,2,3,4}

        for u in range(1, n+1):
            busyColors = {res[v-1] for v in adjList[u]}
            res[u-1] = next(iter(colors - busyColors))

        return res
        