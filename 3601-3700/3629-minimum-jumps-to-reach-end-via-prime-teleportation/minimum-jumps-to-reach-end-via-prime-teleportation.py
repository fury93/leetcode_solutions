MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in factors[a]:
                edges[p].append(i)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            q2 = []
            for i in q:
                if i == n - 1:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1

# todo, doesnt' work, fix later
class Solution2:
    def minJumps(self, nums: List[int]) -> int:
        N = len(nums)
        mx = max(nums)

        allPrimes = self.getPrimes(mx)
        primes = [n for n in nums if allPrimes[n]]
        
        # prime => jumps
        adjList = defaultdict(list)
        
        q = [(0, 0)]
        visited = [False] * N
        visited[0] = True
        while q:
            idx, jumps = q.popleft()
            if idx == N-1:
                return jumps
            
            for nxt in chain([idx-1, idx+1], adjList[idx]):
                if 0 <= nxt < N and not visited[nxt]:
                    q.append((nxt, jumps + 1))
                    visited[nxt] = True

        return -1

    def getPrimes(self, n: int) -> List[List[int]]:
        primes = bytearray([1]) * (n + 1)
        primes[0] = primes[1] = 0
        
        for p in range(2, math.isqrt(n) + 1):
            if primes[p]:
                primes[p*p : n+1 : p] = bytearray(len(range(p*p, n+1, p)))
        return primes