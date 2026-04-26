class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        @cache
        def modpow(v, x):
            return pow(v, x, MOD)

        n = len(nums)
        MOD = 1_000_000_007
        ct = Counter(nums[:k])
        cur = 0
        for v in ct:
            cur = (cur + modpow(v, ct[v])) % MOD
        ans = cur

        for i in range(1, n - k + 1):
            le = nums[i - 1]
            ri = nums[i + k - 1]
            # same value in and out, skipping
            if le == ri: 
                continue
            #
            # left end out of the window
            cur -= modpow(le, ct[le])
            if ct[le] > 1: # do not include le^0
                cur += modpow(le, ct[le] - 1)
            #
            # right end into the window
            if ct[ri]: # do not substract ri^0
                cur -= modpow(ri, ct[ri])
            cur += modpow(ri, ct[ri] + 1)
            cur %= MOD
            #
            # update answer and ct
            ans = max(cur, ans)
            ct[le] -= 1
            if not ct[le]:
                del ct[le]
            ct[ri] += 1
        return ans