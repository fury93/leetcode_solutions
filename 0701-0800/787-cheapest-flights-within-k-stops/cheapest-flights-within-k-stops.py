class Solution:
    # Dijkstra with modiciations
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]
        for u, v, price in flights:
            adjList[u].append((v, price))
        
        q = [(0, -1, src)] # price, stops, city.
        cityStops = [math.inf] * n

        while q:
            price, stops, city = heappop(q)
            # we already have a better way to this city with less stops
            if stops >= cityStops[city] : continue
            cityStops[city] = stops
            
            if city == dst:
                return price
            
            if stops == k: continue # no more stops is availabe

            for nextCity, flyCost in adjList[city]:
                heappush(q, (price + flyCost, stops + 1, nextCity))

        return -1

    # Bellman-Form O(K * E)
    def findCheapestPrice2(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] != float('inf'):
                    tmp[v] = min(tmp[v], dist[u] + w)
            dist = tmp
            
        return dist[dst] if dist[dst] != float('inf') else -1

