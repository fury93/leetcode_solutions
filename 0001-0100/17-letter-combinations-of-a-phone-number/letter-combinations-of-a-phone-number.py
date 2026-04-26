class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def backtrack(comb, i):
            if len(comb) == len(digits):
                res.append(comb)
                return
            
            for ch in d[digits[i]]:
                backtrack(comb + ch, i + 1)

        if digits:
            backtrack("", 0)
        
        return res