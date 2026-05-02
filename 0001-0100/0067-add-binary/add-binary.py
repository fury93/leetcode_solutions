class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = [], 0
        
        for i in range(max(len(a), len(b))):
            print(a, b, ~i)
            d1 = a[~i] if i < len(a) else 0
            d2 = b[~i] if i < len(b) else 0
            carry, d3 = divmod(int(d1) + int(d2) + carry, 2)
            res.append(str(d3))

        if carry:
            res.append(str(carry))
        
        return ''.join(res[::-1])
            