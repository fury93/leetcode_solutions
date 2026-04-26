class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direct, idx = divmod(time, n-1)
        if direct % 2 == 0:
            return 1 + idx
        return n - idx