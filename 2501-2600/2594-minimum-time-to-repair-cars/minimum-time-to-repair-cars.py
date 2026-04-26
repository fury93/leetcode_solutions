class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort(reverse = True)
        l , r = 1, ranks[-1] * cars**2
        
        def isEnoughTime(mins):
            fixedCars = 0
            for rank in ranks:
                # rank * cars^2 = minutes
                fixedCars += int(sqrt(mins // rank))
                if fixedCars >= cars: return True

            return False

        while l < r:
            m = (l + r) // 2
            if isEnoughTime(m):
                r = m
            else:
                l = m + 1

        return l