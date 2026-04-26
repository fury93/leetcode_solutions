class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k-1)

    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int):
        res, l, d = 0, 0, defaultdict(int)
        for r, n in enumerate(nums):
            d[n] +=1
            while len(d) > k:
                d[nums[l]] -=1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l+=1

            res += r - l + 1

        return res