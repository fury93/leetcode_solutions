class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adjList = [[] for _ in range(n)]
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        destination = n - 1
        pq = [(passingFees[0], 0, 0)] # (fee, time, city)
        visitedTime = [math.inf] * n

        while pq:
            fee, time, city = heappop(pq)

            if city == destination:
                return fee

            if time >= visitedTime[city]: continue
            visitedTime[city] = time

            for nextCity, cost in adjList[city]:
                visitTime = time + cost
                if visitTime <= maxTime:
                    heappush(pq, (fee + passingFees[nextCity], visitTime, nextCity))

        return -1