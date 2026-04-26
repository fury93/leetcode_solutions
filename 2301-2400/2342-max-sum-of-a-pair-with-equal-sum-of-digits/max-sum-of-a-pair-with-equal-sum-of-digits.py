class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d, res = {}, -1

        def getSum(val):
            return sum(map(int, str(val)))

        for n in nums:
            digitSum = getSum(n)
            if digitSum in d:
                k = d[digitSum]
                res = max(res, n + k)
                d[digitSum] = max(n, k)
            else:
                d[digitSum] = n
        
        return res