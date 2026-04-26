class Solution:
    def longestPalindrome2(self, s: str) -> int:
        res = 0
        for n in Counter(s).values():
            res += n if not n & 1 or not res & 1 else n-1

        return res

    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)