class BinaryIndexedTree:
    __slots__ = "n", "c"

    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        mod = 10**9 + 7
        ans, n = 0, len(perm)
        tree = BinaryIndexedTree(n + 1)
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * i % mod
        for i, x in enumerate(perm):
            cnt = x - 1 - tree.query(x)
            ans += cnt * f[n - i - 1] % mod
            tree.update(x, 1)
        return ans % mod
        
class Solution2:
    def getPermutationIndex(self, perm: List[int]) -> int:
        smaller_to_right = [0] * len(perm)

        def merge(left, right):
            if left >= right: return [left]

            mid = left + right >> 1
            l_nums, r_nums = merge(left, mid), merge(mid + 1, right)
            merged, p_l, p_r = [], 0, 0

            while p_l < len(l_nums) or p_r < len(r_nums):
                if p_r == len(r_nums) or (p_l < len(l_nums) and perm[l_nums[p_l]] < perm[r_nums[p_r]]):
                    smaller_to_right[l_nums[p_l]] += p_r
                    merged.append(l_nums[p_l])
                    p_l += 1
                else:
                    merged.append(r_nums[p_r])
                    p_r += 1
            
            return merged
        
        merge(0, len(perm) - 1)

        MOD = 10 ** 9 + 7
        fact = [1, 1]
        for i in range(2, len(perm) + 1):
            fact.append(fact[-1] * i % MOD)
        
        return sum(smaller_to_right[i] * fact[len(perm) - i - 1] % MOD for i in range(len(perm))) % MOD