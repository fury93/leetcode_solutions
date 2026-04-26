class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        res = 0
        if k == len(candies):
            return res
        flavors = Counter(candies)
        if k == 0:
            return len(flavors)
        
        for i, flavor in enumerate(candies, start= 1):
            flavors[flavor] -= 1
            if flavors[flavor] == 0:
                del flavors[flavor]
            if i < k: continue
            res = max(res, len(flavors))
            addFlavor = candies[i - k]
            flavors[addFlavor] += 1

        return res