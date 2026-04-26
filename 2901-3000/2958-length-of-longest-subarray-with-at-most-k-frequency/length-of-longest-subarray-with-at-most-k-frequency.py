class Solution:
    def maxSubarrayLength2(self, nums: List[int], k: int) -> int:
        res, l, freq = 0, 0, defaultdict(int)

        for r, num in enumerate(nums):
            freq[num] += 1
            while freq[num] > k:
                freq[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res 

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        moreThanK, l, freq = 0, 0, defaultdict(int)

        for num in nums:
            freq[num] += 1
            
            if freq[num] == k + 1:
                moreThanK += 1
            
            if moreThanK > 0:
                freq[nums[l]] -= 1
                moreThanK -= freq[nums[l]] == k
                l += 1

        return len(nums) - l