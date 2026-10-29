class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order[1:]):
            p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 or size[u] > size[heavy[p]]:
                heavy[p] = u

        head = [0] * n
        pos = [0] * n
        cur = 0

        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in g[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        size2 = 1
        while size2 < n:
            size2 <<= 1

        seg = [0] * (2 * size2)

        for u in range(n):
            seg[size2 + pos[u]] = 1 << (ord(s[u]) - 97)

        for i in range(size2 - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(p, value):
            p += size2
            seg[p] = value
            p >>= 1

            while p:
                seg[p] = seg[p * 2] ^ seg[p * 2 + 1]
                p >>= 1

        def range_query(l, r):
            l += size2
            r += size2
            res = 0

            while l <= r:
                if l & 1:
                    res ^= seg[l]
                    l += 1

                if not (r & 1):
                    res ^= seg[r]
                    r -= 1

                l >>= 1
                r >>= 1

            return res

        def path_query(u, v):
            res = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                res ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            res ^= range_query(pos[u], pos[v])

            return res

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(pos[u], 1 << (ord(c) - 97))
            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_query(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans
        
class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def update(self, x: int, v: int) -> None:
        while x <= self.n:
            self.tree[x] ^= v
            x += BIT.lowbit(x)

    def query(self, x: int) -> int:
        ret = 0
        while x:
            ret ^= self.tree[x]
            x -= BIT.lowbit(x)
        return ret

    def updateRange(self, l: int, r: int, v: int) -> None:
        self.update(l, v)
        self.update(r + 1, v)


class Solution2:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        fa = [[0] * LOG for _ in range(n)]
        dep = [0] * n
        l = [0] * n
        r = [0] * n
        timer = 0

        def dfs(u: int, p: int) -> None:
            nonlocal timer
            timer += 1
            l[u] = timer
            fa[u][0] = p
            for v in g[u]:
                if v == p:
                    continue
                dep[v] = dep[u] + 1
                dfs(v, u)
            r[u] = timer

        dfs(0, 0)

        for j in range(1, LOG):
            for i in range(n):
                fa[i][j] = fa[fa[i][j - 1]][j - 1]

        def lca(u: int, v: int) -> int:
            if dep[u] < dep[v]:
                u, v = v, u
            diff = dep[u] - dep[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = fa[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if fa[u][i] != fa[v][i]:
                    u = fa[u][i]
                    v = fa[v][i]
            return fa[u][0]

        bit = BIT(n + 1)
        s = list(s)
        for i in range(n):
            bit.updateRange(l[i], r[i], 1 << (ord(s[i]) - ord("a")))

        ans = []
        for q in queries:
            op, *rest = q.split()
            if op == "update":
                u, c = int(rest[0]), rest[1]
                bit.updateRange(
                    l[u],
                    r[u],
                    (1 << (ord(s[u]) - ord("a"))) ^ (1 << (ord(c) - ord("a"))),
                )
                s[u] = c
            else:
                u, v = int(rest[0]), int(rest[1])
                w = lca(u, v)
                mask = (
                    bit.query(l[u])
                    ^ bit.query(l[v])
                    ^ (1 << (ord(s[w]) - ord("a")))
                )
                ans.append(mask.bit_count() <= 1)
        return ans