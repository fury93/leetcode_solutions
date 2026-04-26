class Solution:
    def reverseByType(self, s: str) -> str:
        res = [None] * len(s)
        lp = sp = len(s) - 1

        for i, ch in enumerate(s):
            if ch.isalpha():
                while not s[lp].isalpha():
                    lp -= 1
                res[i] = s[lp]
                lp -= 1
            else:
                while s[sp].isalpha():
                    sp -= 1
                res[i] = s[sp]
                sp -=1

        return ''.join(res)