from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        l = len(potions)
        maxPotion = potions[-1]

        for spell in spells:
            minPotion = (success + spell - 1) // spell
            if minPotion > maxPotion:
                res.append(0)
                continue

            index = bisect_left(potions, minPotion)
            res.append(l - index)

        return res
