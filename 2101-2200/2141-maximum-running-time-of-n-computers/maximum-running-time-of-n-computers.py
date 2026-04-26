class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        S = sum(batteries)
        while batteries[-1] > S / n:
            S -= batteries.pop()
            n -= 1
        return S // n