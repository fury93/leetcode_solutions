class Solution:
    def getSum(self, nums: List[int], mod = 1_000_000_007) -> int:

        def dp(dir: int, res = 0)-> int:

            ct, sm = defaultdict(int), defaultdict(int)

            for num in nums:
                ct[num]+= ct[num + dir] + 1
                sm[num]+= sm[num + dir] + num * ct[num + dir] + num
                res    += sm[num + dir] + num * ct[num + dir]

            return res % mod

        return (sum(nums) + dp(-1) + dp(1)) %mod