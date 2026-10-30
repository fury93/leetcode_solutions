class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w, labels[u] == labels[v]))

        done = [k + 1] * n  # min run length among popped states per node
        heap = [(0, 0, 1)]
        last = n - 1

        while heap:
            d, u, r = heappop(heap)
            if r >= done[u]:  # dominated by an earlier (cheaper-or-equal) pop
                continue
            done[u] = r
            if u == last:
                return d
            for v, w, same in graph[u]:
                nr = r + 1 if same else 1
                if nr < done[v]:  # also enforces nr <= k, since done starts at k+1
                    heappush(heap, (d + w, v, nr))

        return -1
        
class Solution2:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end}
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1