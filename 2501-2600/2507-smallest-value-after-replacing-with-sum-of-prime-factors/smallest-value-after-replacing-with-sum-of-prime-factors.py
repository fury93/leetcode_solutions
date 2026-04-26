class Solution:
    def smallestValue(self, n: int) -> int:
        while n > 1:
            factorsSum = sum(self.getPrimeFactors(n))
            if n == factorsSum: break
            n = factorsSum
        return n

    def getPrimeFactors(self, n: int) -> list[int]:
        factors = []
        
        if n % 2 == 0:
            while n % 2 == 0:
                factors.append(2)
                n //= 2
                
        d = 3
        while d * d <= n:
            if n % d == 0:
                while n % d == 0:
                    factors.append(d)
                    n //= d
            d += 2
            
        if n > 1:
            factors.append(n)
            
        return factors