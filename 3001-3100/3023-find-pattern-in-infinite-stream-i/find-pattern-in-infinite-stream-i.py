# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        m = len(pattern)

        queue = deque()

        for _ in range(m):
            queue.append(stream.next())
        
        ovridx = -1
        while True:
            ovridx += 1
            if list(queue) == pattern:
                return ovridx
            test = queue.popleft()
            queue.append(stream.next())