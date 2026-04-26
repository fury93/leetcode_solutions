class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)
        for i in range(len(s)):
            prefix = int(s[:i+1])
            if not Solution.isPrime(prefix): return False
            suffix = int(s[~i:])
            if not Solution.isPrime(suffix): return False
        return True
        
    @staticmethod
    @cache
    def isPrime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        
        for i in range(5, math.isqrt(n)+1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True