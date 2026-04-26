class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj = [[] for _ in range(n)]
        adjRev = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adjRev[v].append((u, w))

        def dijkstra(src, adjList):
            pq = [(0, src)]
            dist = [math.inf] * n
            dist[src] = 0

            while pq:
                d, u = heappop(pq)
                if d > dist[u]: continue

                for v, w in adjList[u]:
                    dv = d + w
                    if dist[v] > dv:
                        dist[v] = dv
                        heappush(pq, (dv, v))

            return dist

        d1 = dijkstra(src1, adj)
        d2 = dijkstra(src2, adj)
        d3 = dijkstra(dest, adjRev)

        res = math.inf
        for i in range(n):
            res = min(res, d1[i] + d2[i] + d3[i])

        return res if res != math.inf else -1