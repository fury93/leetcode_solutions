class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]
        dest = n - 1

        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > dist[u]: continue
            if u == dest:
                return cur_dist

            for v, w in adj[u]:
                new_dist = cur_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return -1