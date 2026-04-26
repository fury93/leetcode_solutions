class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in reversed(range(len(nums))):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        
        return 0   