class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(i: int, fa: int):
            ans[i] = 1
            d[s[i]].append(i)
            for j in g[i]:
                dfs(j, i)
            k = fa
            if len(d[s[i]]) > 1:
                k = d[s[i]][-2]
            if k != -1:
                ans[k] += ans[i]
            d[s[i]].pop()

        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        d = defaultdict(list)
        ans = [0] * n
        dfs(0, -1)
        return ans
        
    def findSubtreeSizes2(self, p: List[int], s: str) -> List[int]:
        n, clds = len(s), defaultdict(set)
        for i in range(n):
            clds[p[i]].add(i)
        res = [0] * n

        def dfs(i, anc={}):
            prv, anc[s[i]] = anc.get(s[i]), i
            res[i] = cnt = 1
            for c in clds[i]:
                dfs(c, anc)
                res[p[c]] += res[c]
            anc[s[i]] = prv
            if prv is not None:
                p[i] = prv

        dfs(0)
        return res