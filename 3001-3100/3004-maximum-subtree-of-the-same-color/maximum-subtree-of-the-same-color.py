from collections import defaultdict
class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        res = 0
        def dfs(v,u):
            nonlocal res
            color, freq, ncolor = colors[v], 1, 1
            for w in G[v]:
                if w == u: continue 
                tcolor, tfreq, tncolor = dfs(w,v)
                if tncolor > 1 or tcolor != color: 
                    ncolor += 1
                freq += tfreq
            if ncolor > 1: return 0, 0, 2
            res = max(res, freq)
            return color, freq, 1 
        dfs(0,-1)
        return res

class Solution2:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        def dfs(node):
            if node not in tree:
                return True, 1
            color = colors[node]
            same, cnt = True, 0
            for child in tree[node]:
                same_child, cnt_child = dfs(child)
                if colors[child] != color or same_child is False:
                    same = False                    
                cnt += cnt_child
            if same:
                ans[0] = max(ans[0], 1 + cnt)
            return same, 1 + cnt

        n = len(colors)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
        ans = [1]
        dfs(0)
        return ans[0]
        