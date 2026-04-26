class Solution:
    def residuePrefixes(self, s: str) -> int:
        res, uniq = 0, set()
        for i, ch in enumerate(s, start = 1):
            uniq.add(ch)
            res += len(uniq) == i % 3
        return res

    def residuePrefixes2(self, s: str) -> int:
        return sum(len(set(s[:i])) == i % 3 for i in range(1, len(s)+1))