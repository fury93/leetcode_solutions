class Solution:
    def minimumLength(self, s: str) -> int:
        # k < 3 => remain k
        # k == 3 => remain 1
        # k == 4 => remain 2
        # k == 5 => remain 1
        return sum(1 if cnt & 1 else 2 for cnt in Counter(s).values())