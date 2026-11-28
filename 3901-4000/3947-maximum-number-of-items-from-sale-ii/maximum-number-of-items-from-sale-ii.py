class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        min_price = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        frequency = [0] * (max_factor + 1)
        for factor, _ in items:
            frequency[factor] += 1

        eligible = [0] * (max_factor + 1)
        for factor in range(1, max_factor + 1):
            if frequency[factor]:
                eligible[factor] = sum(
                    frequency[multiple]
                    for multiple in range(factor, max_factor + 1, factor)
                ) - 1

        deals = []
        for factor, price in items:
            if eligible[factor] > 0 and price < 2 * min_price:
                deals.append((price, eligible[factor]))
        deals.sort()

        answer = 0
        remaining = budget
        for price, capacity in deals:
            purchased = min(capacity, remaining // price)
            answer += 2 * purchased
            remaining -= price * purchased
            if purchased < capacity:
                break

        return answer + remaining // min_price
        
    def maximumSaleItems2(self, items: List[List[int]], budget: int) -> int:
        items.sort(key=lambda x: x[1])
        mx = max(factor for factor, _ in items)
        freq = [0] * (mx + 1)
        for factor, _ in items:
            freq[factor] += 1
        for i in range(1, mx + 1):
            if freq[i] > 0:
                for j in range(i * 2, mx + 1, i):
                    freq[i] += freq[j]

        mn = items[0][1]
        ans = 0
        for factor, price in items:
            if price > mn * 2:
                break
            cnt = freq[factor] - 1
            take = min(cnt, budget // price)
            ans += take * 2
            budget -= take * price
        ans += budget // mn
        return ans