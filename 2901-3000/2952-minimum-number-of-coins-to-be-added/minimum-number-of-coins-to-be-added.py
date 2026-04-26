class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        res, nextExpectedCoin, i = 0, 1, 0
        coins.sort()

        while nextExpectedCoin <= target:
            if i < len(coins) and coins[i] <= nextExpectedCoin:
                nextExpectedCoin += coins[i]
                i += 1
            else:
                nextExpectedCoin += nextExpectedCoin
                res += 1

        return res