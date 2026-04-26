class Solution:
    def maxNumber(self, n: int) -> int:
        msb = 1
        while n > 1:
            msb <<= 1
            n >>= 1
        return msb - 1