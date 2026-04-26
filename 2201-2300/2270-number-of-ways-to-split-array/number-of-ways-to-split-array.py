class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        return sum(prefix[i] >= prefix[-1] - prefix[i] for i in range(len(prefix)-1))

    def waysToSplitArray2(self, nums: List[int]) -> int:
        postfix = sum(nums)
        res, prefix = 0, 0
        for n in nums[:-1]:
            prefix += n
            postfix -= n
            if prefix >= postfix:
                res += 1
        return res
