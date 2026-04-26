class Solution:
    def maximumCost(self, n, highways, k):
        graph = defaultdict(list)
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))

        max_cost = -1  

        for start in range(n):
            pq = [(-0, start, 0)]  
            visited = [False] * n  

            while pq:
                current_fee, current_city, stops = heapq.heappop(pq)
                current_fee = -current_fee 

                visited[current_city] = True

                if stops == k:
                    max_cost = max(max_cost, current_fee)
                    break

                for neighbor, toll in graph[current_city]:
                    if not visited[neighbor]:
                        heapq.heappush(pq, (-(current_fee + toll), neighbor, stops + 1))

        return max_cost

class Solution2:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        
        graph = defaultdict(list)
        for city_a, city_b, cost in highways:
            graph[city_a].append((city_b, cost))
            graph[city_b].append((city_a, cost))
        
        @cache
        def dp(city, bitmask):
            cities_visited = bitmask.bit_count()
            if cities_visited == k + 1:
                return 0
            
            answer = -1
            for nei_city, highway_cost in graph[city]:
                if not (bitmask >> nei_city) & 1:
                    nei_answer = dp(nei_city, bitmask | (1 << nei_city))
                    if nei_answer != -1:
                        answer = max(answer, highway_cost + nei_answer)
            return answer
        
        return max(dp(city, 1 << city) for city in range(n))