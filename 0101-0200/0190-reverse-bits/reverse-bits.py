class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res = (n & 1) << power
            power -= 1
            n >>= 1
        return res
    
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1 | n & 1
            n >>= 1
        return res