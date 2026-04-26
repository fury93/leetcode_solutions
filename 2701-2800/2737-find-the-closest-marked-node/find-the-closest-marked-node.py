class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked = set(marked)
        graph = defaultdict(list)

        for a, b , w in edges:
            graph[a].append((b,w))

        heap = [(0, s)]

        seen = set()

        while heap:
            wgt, node = heapq.heappop(heap)

            if node in seen:
                continue

            seen.add(node)

            if node in marked:
                return wgt



            for child, weight in graph[node]:
                heapq.heappush(heap, (wgt + weight, child))

        return -1
        
class Solution2:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        ## use dijkstra and return the minimum
        ## using dijkstra find minimum distance of all nodes from s
        ## then find the min of distances for nodes that belong to marked array
        graph = {x:[] for x in range(n)}

        for v1, v2, wt in edges:
            graph[v1].append([v2,wt])

        ## dijkstra algorithm
        visited = set()
        pq = []
        dist = {x:float('inf') for x in range(n)}
        dist[s] = 0
        heapq.heappush(pq, (0, s))

        while pq:
            cost, node = heapq.heappop(pq)
            visited.add(node)

            for nei, nei_cost in graph[node]:
                if nei in visited:
                    continue
                new_cost = cost + nei_cost
                if dist[nei] > new_cost:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        ## iterate over the marked list to find min dist of any node from s
        ans = float('inf')
        for node in marked:
            ans = min(ans, dist[node])

        return ans if ans!=float('inf') else -1

        