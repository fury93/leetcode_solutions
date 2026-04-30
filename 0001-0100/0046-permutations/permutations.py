class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permut):
            if len(permut) == len(nums):
                res.append(permut.copy())
                return
            for n in nums:
                if n in permut: continue
                permut.append(n)
                backtrack(permut)
                permut.pop()

        res = []
        backtrack([])
        return res