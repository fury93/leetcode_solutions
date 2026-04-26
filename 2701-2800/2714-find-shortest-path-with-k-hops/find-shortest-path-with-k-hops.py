class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        con = [[] for _ in range(n)]
        for e in edges:
            con[e[0]].append((e[1], e[2]))
            con[e[1]].append((e[0], e[2]))
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        mark = [[False] * (k + 1) for _ in range(n)]
        q = [(0, k, s)]
        while q:
            t, m, x = heappop(q)
            if mark[x][m]:
                continue
            mark[x][m] = True
            if x == d:
                return t
            for y, w in con[x]:
                if w + t < dist[y][m]:
                    dist[y][m] = w + t
                    heappush(q, (dist[y][m], m, y))
                if m and t < dist[y][m - 1]:
                    dist[y][m - 1] = t
                    heappush(q, (dist[y][m - 1], m - 1, y))
        return -1