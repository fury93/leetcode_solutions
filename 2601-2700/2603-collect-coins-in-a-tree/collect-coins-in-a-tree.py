class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        N = len(coins)
        adj = [set() for _ in range(N)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        degree = [len(adj[i]) for i in range(N)]
        leaves = deque([i for i in range(N) if degree[i] == 1 and not coins[i]])
        
        # remove all leaves without coins
        while leaves:
            u = leaves.popleft()
            degree[u] = 0
            for v in adj[u]:
                if degree[v] == 0: continue
                degree[v] -= 1
                if degree[v] == 1 and not coins[v]:
                    leaves.append(v)

        # remove 2 layers of tree
        for _ in range(2):
             leaves = deque([i for i in range(N) if degree[i] == 1])
             for u in leaves:
                degree[u] = 0
                for v in adj[u]:
                    if degree[v] > 0:
                        degree[v] -= 1

        
        remainNodes = N - degree.count(0)
        if remainNodes <= 1:
            return 0

        return (remainNodes - 1) * 2