class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        left, right = Counter(), Counter(nums)
        for i, n in enumerate(nums):
            left[n] += 1
            right[n] -= 1
            if right[n] == 0:
                del right[n]
            res[i] = len(left) - len(right)

        return res

    def distinctDifferenceArray2(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]