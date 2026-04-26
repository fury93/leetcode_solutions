class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        nextExpectedValue = 1

        for coin in sorted(coins):
            if coin > nextExpectedValue: break
            nextExpectedValue += coin

        return nextExpectedValue
