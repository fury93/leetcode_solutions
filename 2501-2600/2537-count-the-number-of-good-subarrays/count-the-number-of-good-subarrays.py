class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cntMap = defaultdict(int)
        invalidSub,pairCnt = 0,0
        l = 0
        for r in range(n):
            pairCnt += cntMap[nums[r]]
            cntMap[nums[r]] += 1
            while l<=r and pairCnt >= k:
                pairCnt -= (cntMap[nums[l]]-1)
                cntMap[nums[l]] -= 1
                l += 1
            invalidSub += (r-l+1)
        return n*(n+1)//2 - invalidSub