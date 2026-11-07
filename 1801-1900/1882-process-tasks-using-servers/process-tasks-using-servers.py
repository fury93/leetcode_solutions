class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res, unavailable = [], []
        available = [(weight, id) for id, weight in enumerate(servers)]
        heapify(available)

        for time, task in enumerate(tasks):
            while unavailable and unavailable[0][0] == time:
                _, weight, id = heappop(unavailable)
                heappush(available, (weight, id))

            if len(available) > 0:
                weight, id = heappop(available)
                heappush(unavailable, (time + task, weight, id))
                res.append(id)
            else:
                finishTime, weight, id = heappop(unavailable)
                heappush(unavailable, (finishTime + task, weight, id))
                res.append(id)

        return res

    def assignTasks2(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        servers = [(weight, id) for id, weight in enumerate(servers)]
        heapify(servers)
        tasks = iter(tasks)
        processServers = []

        time = 0
        while tasks:
            # release available servers after processing
            while processServers and processServers[0][0] == time:
                _, weight, id = heappop(processServers)
                heappush(servers, (weight, id))

            if len(servers) > 0:
                task = next(tasks, None)
                if not task: break
                weight, id = heappop(servers) #server with less weight
                heappush(processServers, (time + task, weight, id))
                res.append(id)
                
            time +=1

        return res

    