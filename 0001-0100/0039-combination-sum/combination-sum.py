class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, i):
            comb_sum = sum(comb)
            
            if comb_sum > target:
                return
            elif comb_sum == target:
                res.append(comb.copy())
                return

            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                backtrack(comb, j)
                comb.pop()
        
        res = []
        backtrack([], 0)

        return res
