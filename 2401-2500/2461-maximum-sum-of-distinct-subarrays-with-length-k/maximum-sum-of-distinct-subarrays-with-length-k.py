class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, curSum,  cnt = 0, 0, defaultdict(int)
        for i, n in enumerate(nums, start = 1):
            cnt[n] += 1
            curSum += n
            if i < k: continue
            
            if len(cnt) == k:
                res = max(res, curSum)

            remove = nums[i - k]
            cnt[remove] -= 1
            if cnt[remove] == 0:
                del cnt[remove]
            curSum -= remove

        return res