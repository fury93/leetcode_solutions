class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res, s, b = 0, 0, set(banned)
        for i in range(1, n+1):
            if s + i > maxSum: break
            if i not in b:
                s += i
                res += 1

        return res
