class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxLen = 0
        for i in range(len(nums)):
            curLen = 0
            while nums[i] >= 0:
                # i, nums[i] = nums[i], -1 # DOESN'T WORK
                nums[i], i = -1, nums[i]
                #print(i, nums[i], nums)
                curLen += 1
            maxLen = max(maxLen, curLen)

        return maxLen