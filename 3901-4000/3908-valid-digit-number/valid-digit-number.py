class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        nstr = str(n)
        xstr = str(x)
        return xstr in nstr and not nstr.startswith(xstr)