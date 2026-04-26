# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        
        num, target, ans, n = 0, 0, 0, len(pattern)
        mask = (1<<(n-1))-1

        for bit in pattern:                       # <-- 1.
            target = 2*target + bit               #

        while num != target or ans < n:           # <-- 2.
            num = 2*(num&mask) + stream.next()    #
            ans+= 1

        return ans-n                              # <-- 3.