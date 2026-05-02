class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k: return -1
        return (n ^ k).bit_count()