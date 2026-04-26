class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, l, d = 0, 0, defaultdict(int)
        
        for r, f in enumerate(fruits):
            d[f] +=1
            while len(d) > 2:
                d[fruits[l]] -=1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l +=1
            # res = max(res, sum(d.values()))
            res = max(res, r - l + 1)

        return res