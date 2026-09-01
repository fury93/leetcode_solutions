class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        return requests[0] + sum(abs(cur - nxt) for cur, nxt in pairwise(requests))