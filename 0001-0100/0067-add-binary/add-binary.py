class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        return bin(a + b)[2:]

    def addBinary2(self, a: str, b: str) -> str:
        res, carry = [], 0
        
        for i in range(max(len(a), len(b))):
            d1 = a[~i] if i < len(a) else 0
            d2 = b[~i] if i < len(b) else 0
            carry, d3 = divmod(int(d1) + int(d2) + carry, 2)
            res.append(str(d3))

        if carry:
            res.append(str(carry))
        
        return ''.join(res[::-1])
            