class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(comb, i):
            comb_sum = sum(comb)
            
            if comb_sum > target:
                return
            elif comb_sum == target:
                res.append(comb.copy())
                return

            for j in range(i, len(candidates)):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                if comb_sum + candidates[j] > target:
                    break
                comb.append(candidates[j])
                backtrack(comb, j+1)
                comb.pop()
        
        backtrack([], 0)

        return res