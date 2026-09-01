class Solution:
    def countValidPrefixes(self, s: str) -> int:
        res, ones, zeros = 0, 0, 0
        for ch in s:
            if ch == "0":
                zeros += 1
            else:
                ones += 1

            if abs(ones - zeros) <= 1:
                res += 1

        return res

            