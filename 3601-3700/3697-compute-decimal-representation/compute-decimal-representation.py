class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res, tens = [], 0

        while n > 0:
            n ,rem = divmod(n, 10)
            if rem:
                res.append(rem * 10**tens)
            tens += 1

        return res[::-1]
            