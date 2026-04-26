class Solution:
    #  meta asks for 560 are returning a list of all subarrays that sum to k (instead of the number of such subarrays),
    # or the array contains non-negative numbers (sliding window)
    def subarraySum(self, nums: List[int], k: int) -> int:
        d, res, curSum = defaultdict(int, {0: 1}), 0, 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += d[diff]
            d[curSum] += 1

        return res
