class Solution:
    def maxScore(self, prices: List[int]) -> int:
        price_sum_by_difference = defaultdict(int)
        for index, price in enumerate(prices):
            difference = price - index
            price_sum_by_difference[difference] += price 
        return max(price_sum_by_difference.values())