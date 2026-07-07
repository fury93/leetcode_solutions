class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [d for d in str(n) if d != '0']
        if not digits:
            return 0
        
        val = int(''.join(digits))
        sm = sum(d for d in map(int, digits))
        
        return val * sm