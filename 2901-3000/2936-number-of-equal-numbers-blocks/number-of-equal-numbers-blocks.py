# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution:
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        def helper(l: int, val_l: int, r: int, val_r: int):
            if val_l == val_r:
                return 1
            if l + 1 == r:
                return 2
            m = (l + r) // 2
            val_m = nums.at(m)
            return helper(l, val_l, m, val_m) + helper(m, val_m, r, val_r) - 1
        return helper(0, nums.at(0), nums.size() - 1, nums.at(nums.size() - 1))