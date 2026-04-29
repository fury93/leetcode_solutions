class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(comb, l, r):
            if len(comb) == 2 * n:
                res.append(comb)
                return
            if l < n:
                backtrack(comb + '(', l + 1, r)
            if r < l:
                backtrack(comb + ')', l, r + 1)
            
        res = []
        backtrack('', 0, 0)
        
        return res