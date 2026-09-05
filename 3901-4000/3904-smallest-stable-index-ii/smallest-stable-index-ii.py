class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi = nums[0]
        mint = float("inf")
        mini = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            mint = min(mint,nums[i])
            mini[i]=mint
        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            if maxi-mini[i]<=k:
                return i
        return -1
        
    def firstStableIndex2(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minValue = [inf] * (n - 1) + [nums[-1]]
        for i in range(n - 2, -1, -1):
            minValue[i] = min(minValue[i + 1], nums[i])

        maxValue = 0
        for i in range(n):
            maxValue = max(maxValue, nums[i])
            if maxValue - minValue[i] <= k:
                return i
        return -1