class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (-1, 1), (1, -1),
        ]
        
        cnt = Counter()
        for r, c in product(range(R), range(C)):
            for dr, dc in directions:
                nr, nc, curn = r, c, 0
                while 0 <= nr < R and 0 <= nc < C:
                    curn = curn * 10 + mat[nr][nc]
                    if curn > 10:
                        cnt[curn] += 1
                    nr, nc = nr + dr, nc + dc

        nums = sorted(cnt, key=lambda x: (cnt[x], x), reverse = True)
        for num in nums:
            if num > 10 and self.isPrime(num): return num

        return -1

    def isPrime(self, n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        
        for i in range(5, math.isqrt(n)+1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True