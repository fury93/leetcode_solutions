class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices 
    
    def finalPrices2(self, prices: List[int]) -> List[int]:
        res = [None] * len(prices)
        stack = []

        for i, p in enumerate(prices):
            while stack and stack[-1][0] >= p:
                val, index = stack.pop()
                res[index] = val - p
            stack.append((p, i))
        
        while stack:
            val, index = stack.pop()
            res[index] = val

        return res

