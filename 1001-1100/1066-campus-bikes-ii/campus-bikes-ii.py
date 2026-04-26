class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)
        # 0 ~ m - 1  workers
        # m ~ m + n - 1 bikes
        s = m + n # dummy source
        t = s + 1 # dummy sink
        num_nodes = m + n + 2
        g =[[] for _ in range(num_nodes)]
        prevv = [None] * num_nodes
        preve = [None] * num_nodes
        
        def add_edge(from_node, to_node, cap, cost):
            g[from_node].append([to_node, cap, cost, len(g[to_node])])
            # reverse edge
            g[to_node].append([from_node, 0, -cost, len(g[from_node]) - 1])
        
        # find minimum cost to flow f from s to t
        def min_cost_flow(s, t, f):
            res = 0
            # Bellman-Ford
            while f > 0:
                dist = [float('inf')] * (m + n + 2)
                dist[s] = 0
                update = True
                while update:
                    update = False
                    for v in range(num_nodes):
                        if dist[v] == float('inf'):
                            continue
                        for i in range(len(g[v])):
                            edge = g[v][i]
                            # if there is capacity left on this edge and 
                            # it costs less to go to the next node from here
                            if edge[1] > 0 and dist[edge[0]] > dist[v] + edge[2]:
                                dist[edge[0]] = dist[v] + edge[2]
                                prevv[edge[0]] = v
                                preve[edge[0]] = i
                                update = True
                assert dist[t] != float('inf')
                d = f
                v = t
                while v != s:
                    d = min(d, g[prevv[v]][preve[v]][1])
                    v = prevv[v]
                f -= d
                res += d * dist[t]
                v = t
                while v != s:
                    edge = g[prevv[v]][preve[v]]
                    edge[1] -= d
                    g[v][edge[3]][1] += d
                    v = prevv[v]
            return res
        
        for i in range(m):
            for j in range(n):
                x1, y1 = workers[i]
                x2, y2 = bikes[j]
                c = abs(x1 - x2) + abs(y1 - y2)
                add_edge(i, m + j, 1, c)
        for i in range(m):
            add_edge(s, i, 1, 0)
        for i in range(n):
            add_edge(m + i, t, 1, 0)

        return min_cost_flow(s, t, m)