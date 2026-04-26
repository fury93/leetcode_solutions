class Solution:
    def numSub(self, s: str) -> int:
        return sum((len(x) * (len(x) + 1))//2 for x in s.split('0')) % (pow(10, 9) + 7)

    def numSub2(self, s: str) -> int:
        res, l = 0, 0
        for r, c in enumerate(s):
            if c == '1':
                res += r - l + 1
            else:
                l = r + 1

        return res % (pow(10, 9) + 7)