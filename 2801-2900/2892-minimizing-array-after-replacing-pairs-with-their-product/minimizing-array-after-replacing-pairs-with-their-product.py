class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        count, last = 0, None
        for n in nums:
            if n == 0: return 1
            if last and last * n <= k:
                last *= n
            else:
                count += 1
                last = n
        return count