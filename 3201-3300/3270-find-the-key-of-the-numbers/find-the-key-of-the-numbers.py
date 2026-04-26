class Solution:
    # Math
    def generateKey2(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        for i in range(4):
            num1, rem1 = divmod(num1, 10)
            num2, rem2 = divmod(num2, 10)
            num3, rem3 = divmod(num3, 10)
            decimalPlace = 10**i
            res += min(rem1, rem2, rem3) * decimalPlace

        return res

    # Convert to string, ye15
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        vals = [str(x).zfill(4) for x in (num1, num2, num3)]
        return int("".join(map(min, zip(*vals))))