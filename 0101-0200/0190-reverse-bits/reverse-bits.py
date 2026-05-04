class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res |= (n & 1) << power
            power -= 1
            n >>= 1
        return res
    
    def reverseBits2(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1 | n & 1
            n >>= 1
        return res

# Byte by Byte with Memoization
class Solution2:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xFF) << power
            n = n >> 8
            power -= 8
        return ret

    # memoization with decorator
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023

# Mask and Shift
class Solution3:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n