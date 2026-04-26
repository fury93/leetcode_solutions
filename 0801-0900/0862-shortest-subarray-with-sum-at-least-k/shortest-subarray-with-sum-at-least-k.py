class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # Monotonic increasing queue with indexes
        min_queue = collections.deque()
        prefix = list(accumulate(A, initial=0))
        res = len(A) + 1
        
        for i, cur_sum in enumerate(prefix):
            # Keep queue increasing (the first value is the minimum for a window)
            while min_queue and prefix[min_queue[-1]] > cur_sum:
                min_queue.pop()
            min_queue.append(i)

            # Update result
            while min_queue and cur_sum - K >= prefix[min_queue[0]]:
                res = min(res, i - min_queue.popleft())
        
        return res if res <= len(A) else -1