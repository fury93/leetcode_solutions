class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        res, maxUniq = 0, - math.inf
        nums.sort()

        for n in nums:
            nextMaxUniq = min(max(maxUniq + 1, n - k), n + k)

            if nextMaxUniq > maxUniq:
                res += 1
                maxUniq = nextMaxUniq

        return res