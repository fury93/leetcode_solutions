class Solution:
    # Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adjList[u].append((v, w))

        travelTime = dict()
        q = [(0, k)]

        while q:
            curTime, u = heappop(q)
            if u in travelTime: continue

            travelTime[u] = curTime
            if len(travelTime) == n: break

            for v, w in adjList[u]:
                if v not in travelTime:
                    heappush(q, (curTime + w, v))

        return -1 if len(travelTime) < n else max(travelTime.values())

    # SPFA
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        bestTime = [0] + [math.inf] * n
        bestTime[k] = 0

        q = deque([k])
        inQueue = [False] * (n + 1)
        inQueue[k] = True

        while q:
            u = q.popleft()
            inQueue[u] = False

            for v, w in adjList[u]:
                newTime = bestTime[u] + w
                
                if newTime < bestTime[v]:
                    bestTime[v] = newTime
                    if not inQueue[v]:
                        q.append(v)
                        inQueue[v] = True
               

        res = max(bestTime)
        return -1 if res == math.inf else res