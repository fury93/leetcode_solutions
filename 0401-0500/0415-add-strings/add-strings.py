class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, i, carry = [], 0, 0

        for i in range(max(len(num1), len(num2))):
            d1 = int(num1[~i]) if i < len(num1) else 0
            d2 = int(num2[~i]) if i < len(num2) else 0

            carry, d3 = divmod(d1+d2+carry, 10)
            res.append(str(d))

        if carry:
            res.append(str(carry))

        return "".join(res[::-1])

    def addStrings(self, num1: str, num2: str) -> str:
        i1, i2, carry, res = len(num1)-1, len(num2)-1, 0, deque()
        
        while i1 >=0 or i2 >=0 or carry:
            d1 = int(num1[i1]) if i1 >= 0 else 0
            d2 = int(num2[i2]) if i2 >= 0 else 0

            carry, d = divmod(d1+d2+carry, 10)
            res.appendleft(str(d))
            i1 -=1
            i2 -=1

        return "".join(res)