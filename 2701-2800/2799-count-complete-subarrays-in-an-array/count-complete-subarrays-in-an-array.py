class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res, uniqCnt, l, d = 0, len(set(nums)), 0, defaultdict(int)
        for n in nums:
            d[n] += 1

            while len(d) == uniqCnt:
                d[nums[l] ] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            res += l
            
        return res

