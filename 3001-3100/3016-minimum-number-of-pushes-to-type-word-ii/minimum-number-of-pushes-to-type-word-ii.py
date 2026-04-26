class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        return sum((i // 8 + 1) * f for i, f in enumerate(freq))