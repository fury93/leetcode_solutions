class Solution:
    def minimumFlips(self, n: int) -> int:
        nb = bin(n)[2:]
        rnb = nb[::-1]
        return sum(b1 != b2 for b1, b2 in zip(nb, rnb))