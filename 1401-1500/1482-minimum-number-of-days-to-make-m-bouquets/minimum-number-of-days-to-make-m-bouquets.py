class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1

        def isEnoughDays(days):
            flowers, bouquets = 0, 0
            for d in bloomDay:
                flowers = flowers + 1 if d <= days else 0
                if flowers == k:
                    bouquets += 1
                    if bouquets == m: break
                    flowers = 0
            
            return bouquets == m

        l, r = 1, max(bloomDay)
        while l < r:
            days = (l+r)//2
            if isEnoughDays(days):
                r = days
            else:
                l = days + 1
        
        return l


        