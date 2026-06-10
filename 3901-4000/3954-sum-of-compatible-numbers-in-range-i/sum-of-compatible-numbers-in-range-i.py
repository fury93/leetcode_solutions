class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        start = max(1, n - k)
        end = n + k
        return sum(x for x in range(start, end + 1) if (n & x) == 0)