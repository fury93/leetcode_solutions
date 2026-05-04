class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res, even, odd = [], 0, 0
        for n in reversed(nums):
            if n & 1:
                odd += 1
                res.append(even)
            else:
                even += 1
                res.append(odd)
        
        return res[::-1]

