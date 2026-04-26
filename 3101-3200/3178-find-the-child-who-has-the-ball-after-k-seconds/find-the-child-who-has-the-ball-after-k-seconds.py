class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        direction, pos = divmod(k, n-1)
        return pos if direction % 2 == 0 else n - 1 - pos