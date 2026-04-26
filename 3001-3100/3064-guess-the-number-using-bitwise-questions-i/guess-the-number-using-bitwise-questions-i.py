# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:
class Solution:
    def findNumber(self) -> int:
        return sum(commonSetBits(1 << bit) << bit for bit in range(31))
