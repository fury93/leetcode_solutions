class Solution:
    def minimumTime(self, power: List[int]) -> int:
        @cache
        def dp(mask):
            rest = [i for i in range(len(power)) if mask & (1<<i)==0]
            if not len(rest): return 0
            gain = len(power)-len(rest)+1
            return min(dp(mask|(1<<i))+(power[i]+(gain-1))//gain for i in rest)
        return dp(0)