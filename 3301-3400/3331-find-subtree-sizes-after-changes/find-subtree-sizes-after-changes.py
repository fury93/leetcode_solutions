class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
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