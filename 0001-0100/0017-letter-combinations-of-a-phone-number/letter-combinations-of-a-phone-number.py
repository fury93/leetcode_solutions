#O(4^N * N)
class Solution:
    LETTERS = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(comb, i):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return
            
            for ch in self.LETTERS[digits[i]]:
                comb.append(ch)
                backtrack(comb, i + 1)
                comb.pop()

        res = []
        if digits:
            backtrack([], 0)
        
        return res