class Solution:
    def concatHex36(self, n: int) -> str:
        SYMBOLS = string.digits + string.ascii_uppercase
        def toBase(n, base):
            if n == 0: return "0"
            
            res = []
            while n > 0:
                n, rem = divmod(n, base)
                res.append(SYMBOLS[rem])
            return ''.join(reversed(res))

        return toBase(n**2, 16) + toBase(n**3, 36)