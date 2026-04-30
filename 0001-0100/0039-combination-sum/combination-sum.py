class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, i, remain):
            if remain == 0:
                res.append(comb.copy())
                return
            elif remain < 0:
                return

            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                backtrack(comb, j, remain - candidates[j])
                comb.pop()
        
        res = []
        backtrack([], 0, target)

        return res
