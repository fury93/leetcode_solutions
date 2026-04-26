class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(pos - s.index(ch)) for pos, ch in enumerate(t))