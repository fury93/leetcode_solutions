class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        return sum(val * cnt for val, cnt in Counter(nums).items() if cnt % k == 0)