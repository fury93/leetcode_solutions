class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        
        @cache
        def construct_string(i):
            if i == len(target):
                return 0
            min_cost = float('inf')
            for j, word in enumerate(words):
                if target.startswith(word, i):
                    min_cost = min(min_cost, costs[j] + construct_string(i + len(word)))
            return min_cost
        
        min_cost = construct_string(0)
        return min_cost if min_cost != float('inf') else -1
        
        
class Solution2:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        dp = [0] + [inf] * n
        for i in range(n):
            for w, c in zip(words, costs):
                if target[i:i+len(w)] == w:
                    dp[i+len(w)] = min(dp[i+len(w)], dp[i] + c)
        return dp[-1] if dp[-1] != inf else -1