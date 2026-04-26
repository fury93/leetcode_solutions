class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) // 2)
        return -1 if x % 1 else int(x)
        