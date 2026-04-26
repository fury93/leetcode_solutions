class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for n in nums:
            if n % 2 == 0:
                factors.add(2)
                while n % 2 == 0:
                    n //= 2
            
            d = 3
            while d * d <= n:
                if n % d == 0:
                    factors.add(d)
                    while n % d == 0:
                        n //= d
                d += 2
            
            if n > 1:
                factors.add(n)
        
        return len(factors)


    def distinctPrimeFactors2(self, nums: List[int]) -> int:
        factors = set()
        for n in nums:
            d = 2
            while d*d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            
            if n > 1:
                factors.add(n)
        
        return len(factors)