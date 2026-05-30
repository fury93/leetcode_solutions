class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        for key in cnt:
            if cnt[key] > k:
                cnt[key] = k
        return list(cnt.elements())