class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res, s1, s2 = [], set(), set()
        for a, b in zip(A, B):
            s1.add(a)
            s2.add(b)
            res.append(len(s1 & s2))
        return res
