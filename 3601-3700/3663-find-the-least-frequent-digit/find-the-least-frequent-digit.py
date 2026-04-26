class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = Counter(str(n))
        return int(min(cnt.keys(), key = lambda k: (cnt[k], k)))