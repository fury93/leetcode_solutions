class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        cnt = Counter(nums)
        uniq = set(key for key in cnt if cnt[key] == 1)
        
        if k == 1:
            return max(uniq, default = -1)
        
        if nums[0] not in uniq:
            return nums[-1] if nums[-1] in uniq else -1

        return nums[0] if nums[-1] not in uniq else max(nums[0], nums[-1])