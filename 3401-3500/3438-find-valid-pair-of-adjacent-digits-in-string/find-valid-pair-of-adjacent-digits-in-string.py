class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        for a, b in pairwise(s):
            if a != b and cnt[a] == int(a) and cnt[b] == int(b):
                return a + b
        return ''