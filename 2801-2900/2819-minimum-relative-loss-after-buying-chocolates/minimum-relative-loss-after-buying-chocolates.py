class Solution:
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:

        prices.sort()
        n, ans = len(prices), []
        acc = list(accumulate(prices, initial = 0))

        for k, m in queries:

            split = min(bisect_left(prices, k), m)

            cut = bisect_left(range(split), 2*k, 
                               key = lambda x: prices[x]+ prices[n - m + x])
 
            ans.append((m - cut) * 2*k + acc[n - m + cut] + acc[cut]  - acc[n])

        return ans