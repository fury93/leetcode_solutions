class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) < 2: return False
        digits = list(map(int, s))
        while len(digits) > 2:
            newDigits = []
            for a, b in pairwise(digits):
                newDigits.append((a + b) % 10)
            digits = newDigits

        return digits[0] == digits[1]