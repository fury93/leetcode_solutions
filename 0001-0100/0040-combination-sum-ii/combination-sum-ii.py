class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(comb, start, remain):
            if remain == 0:
                res.append(comb.copy())
                return
            elif remain < 0:
                return

            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                comb.append(candidates[j])
                backtrack(comb, j + 1, remain - candidates[j])
                comb.pop()
        
        backtrack([], 0, target)

        return res