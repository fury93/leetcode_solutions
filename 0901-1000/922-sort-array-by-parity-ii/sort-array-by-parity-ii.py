class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        even, odd = 0, 1
        
        for n in nums:
            if n % 2:
                res[odd] = n
                odd += 2
            else:
                res[even] = n
                even += 2
        return res