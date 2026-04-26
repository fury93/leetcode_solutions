class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits) - 1))
        