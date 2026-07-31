class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        res = 0
        for _ in range(n):
            d = s if s <= 9 else 9
            s -= d
            res = res * 10 + d

        return res if s == 0 else -1