class Solution:
    def makePalindrome(self, s: str) -> bool:
        swapsAllowed, l, r = 2, 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            elif swapsAllowed > 0:
                swapsAllowed -= 1
                l, r = l + 1, r - 1
            else: return False

        return True