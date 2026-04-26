class Solution:
    def minimumChairs(self, s: str) -> int:
        res, cur = 0, 0
        for ch in s:
            if ch == 'E':
                cur += 1
            else:
                cur -= 1
            res = max(res, cur)
        return res