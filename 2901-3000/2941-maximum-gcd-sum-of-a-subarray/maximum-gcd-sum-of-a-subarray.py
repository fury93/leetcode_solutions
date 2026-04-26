class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        f = []
        ans = 0
        for i, v in enumerate(nums):
            g = []
            for j, x in f:
                y = gcd(x, v)
                if not g or g[-1][1] != y:
                    g.append((j, y))
            f = g
            f.append((i, v))
            for j, x in f:
                if i - j + 1 >= k:
                    ans = max(ans, (s[i + 1] - s[j]) * x)
        return ans
        
class Solution2:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        # Sequence of pairs (idx, gcd), both strictly increasing.
        gcds = []
        prefix_sum = [0]
        best = 0
        for i, x in enumerate(nums):
            prefix_sum.append(prefix_sum[-1] + x)
            new_gcds = []
            for j, g in gcds + [(i, x)]:
                ng = gcd(g, x)
                # Skipping duplicates.
                if not new_gcds or new_gcds[-1][1] != ng:
                    new_gcds.append((j, ng))
            gcds = new_gcds
            for j, g in gcds:
                if i - j + 1 < k: break
                best = max(best, (prefix_sum[-1] - prefix_sum[j]) * g)
        return best

        