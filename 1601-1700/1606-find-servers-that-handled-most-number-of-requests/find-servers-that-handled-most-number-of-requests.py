class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        count = [0] * k
        busy, free = [], list(range(k))

        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                heapq.heappush(free, i + (server_id - i) % k)

            if free:
                busy_id = heapq.heappop(free) % k
                heapq.heappush(busy, (start + load[i], busy_id))
                count[busy_id] += 1

        max_job = max(count)
        return [i for i, n in enumerate(count) if n == max_job]