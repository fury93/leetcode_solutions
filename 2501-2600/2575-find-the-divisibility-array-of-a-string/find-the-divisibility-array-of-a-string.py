class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        remainder = 0
        for i in range(len(word)):
            remainder = (remainder * 10 + int(word[i])) % m
            res[i] = int(remainder == 0)

        return res