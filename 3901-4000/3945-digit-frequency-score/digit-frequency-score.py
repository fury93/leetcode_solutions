class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        cnt = Counter(str(n))
        return sum(int(k) * v for k, v in cnt.items())