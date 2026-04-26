class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(ch.islower() and ch.upper() in chars for ch in chars)