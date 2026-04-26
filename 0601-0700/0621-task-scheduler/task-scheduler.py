class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        q, maxHeap, time = deque(), [], 0
        for task, cnt in Counter(tasks).items():
            maxHeap.append(-cnt)
        heapify(maxHeap)
        
        while maxHeap or q:
            time +=1
            if q and q[0][0] == time:
                heappush(maxHeap, q.popleft()[1])
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    q.append((time + n + 1, cnt))
        
        return time

