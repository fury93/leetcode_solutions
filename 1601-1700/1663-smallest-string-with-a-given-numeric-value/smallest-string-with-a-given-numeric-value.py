class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, mid = divmod(k - n, 25)
        return ('a' * (n - z - 1) + chr(ord('a')+mid) if z < n else '') + 'z' * z