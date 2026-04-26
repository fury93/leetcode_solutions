class Solution:
    def validStrings(self, n: int) -> List[str]:
        def generate(i):
            if i == n:
                res.append(''.join(digits))
                return
            
            if digits[i-1] != '0':
                digits[i] = '0'
                generate(i+1)
            digits[i] = '1'
            generate(i+1)
            
        res, digits = [], [None] * n
        generate(0)
        return res
            
