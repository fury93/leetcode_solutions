class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        max_len = max(len(a), len(b))+1
        
        for i in range(1, max_len):
            d1 = a[-i] if i <= len(a) else 0
            d2 = b[-i] if i <= len(b) else 0
            carry, d3 = divmod(int(d1) + int(d2) + carry, 2)
            res = str(d3) + res

        return str(carry) + res if carry else res
            