class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        prefix = 0
        postfix = sum(nums)

        for n in nums:
            prefix += n
            postfix -= n
            if n == 0:
                if prefix == postfix:
                    res += 2
                if abs(prefix - postfix) == 1:
                    res += 1

        return res




