class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1 = sum(v for v in range(1, n+1) if v % m != 0)
        n2 = sum(v for v in range(1, n+1) if v % m == 0)
        return n1 - n2
        