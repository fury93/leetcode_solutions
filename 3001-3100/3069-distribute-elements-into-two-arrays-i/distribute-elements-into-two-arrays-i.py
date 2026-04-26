class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n1, n2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if n1[-1] > n2[-1]:
                n1.append(nums[i])
            else:
                n2.append(nums[i])
        return n1 + n2