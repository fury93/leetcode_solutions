class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res, cnt1 = [], Counter(digits)
        for n in range(100, 999, 2):
            cnt2 = Counter(int(d) for d in str(n))
            if cnt1 >= cnt2:
                res.append(n)
        return res