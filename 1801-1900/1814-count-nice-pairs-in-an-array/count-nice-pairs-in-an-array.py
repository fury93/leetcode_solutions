class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [n - int(str(n)[::-1]) for n in nums]
        res = 0
        for n in Counter(nums).values():
            res += n*(n-1)//2 
        return res % (10**9 + 7)

    
    def countNicePairs2(self, nums: List[int]) -> int:
        res, d = 0, defaultdict(int)
        for i, n in enumerate(nums):
            k = n - int(str(n)[::-1])
            res += d[k]
            d[k] += 1
        return res % (10**9 + 7)