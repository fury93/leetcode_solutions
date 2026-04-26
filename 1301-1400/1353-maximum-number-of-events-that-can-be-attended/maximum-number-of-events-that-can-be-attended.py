class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans
        
    def maxEvents2(self, events: List[List[int]]) -> int:
        events.sort()
        #print(len(events), events)
        blockStart = prevStart = 0
        for i in range(len(events)):
            if events[i][0] == blockStart:
                if prevStart == events[i][1]:
                    events[i] = [10**5+1, 10**5]
                else:
                    prevStart += 1
                    events[i][0] = prevStart
            else:
                blockStart = prevStart = events[i][0]

        heapify(events)
        res, curStart = 0, 0
        while events:
            #print('events', events)
            if events[0][0] < curStart:
                start, end = heappop(events)
                if curStart <= end:
                    heappush(events, [curStart, end])
                if not events: break
        
            start, end = heappop(events)
            #print(bool(curStart <= end), curStart, start, end)
            if curStart <= end and start <= end:
                res += 1
                curStart = max(curStart, start) + 1

        return res


        heap, availableFrom = [], -math.inf
        
        for start, end in events:
            start = max(availableFrom, start)
            if start <= end:
                heappush(heap, (start, end))
                availableFrom = start + 1

        res, availableFrom = 0, heap[0][0]
        while heap:
            start, end = heappop(heap)
            if availableFrom <= end:
                res += 1
                availableFrom = max(availableFrom, start) + 1

        return res
        
        while heap:
            # remove events we can't able to attend
            while events and events[0][1] < availableFrom:
                heappop(events)

            # case [[1,5],[1,5],[1,5],[2,3],[2,3]] => change start time for events to update priority
            # firstly need to process elements with smallest start and end time
            while events and events[0][0] <= availableFrom:
                heapreplace(events, [availableFrom, events[0][1]])
                
            if events:
                start, end = heappop(events)
                res += 1
                availableFrom = max(start + 1, availableFrom + 1)
        
        return res