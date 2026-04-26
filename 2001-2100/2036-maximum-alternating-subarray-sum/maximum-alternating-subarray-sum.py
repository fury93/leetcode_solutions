class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        add = nums[0]
        sub = float('-inf')
        rst = add

        for num in nums[1:]:
            add, sub = max(sub + num, num), add - num
            rst = max(rst, add, sub)
        
        return rst
        
class Solution2:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        max_sum = pos = nes = float('-inf')
        for i, num in enumerate(nums):
            pos, nes = max(nes + num, num), pos - num
            max_sum = max(max_sum, pos, nes)
        return max_sum