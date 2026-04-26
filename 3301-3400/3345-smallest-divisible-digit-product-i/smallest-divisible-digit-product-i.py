class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digitsProd = reduce(lambda p, v: p * int(v), str(n), 1)
            if digitsProd % t == 0:
                return n
            n += 1