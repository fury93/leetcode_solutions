class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0,  0, len(people) - 1

        while l <= r:
            res += 1
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
        
        return res

    #remove places and it will be solution for taks with no limit for seats
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0

        while l <= r:
            boatLimit = limit
            places = 2
            while l <= r and people[r] <= boatLimit and places:
                boatLimit -= people[r]
                places -= 1
                r -= 1

            while l <= r and people[l] <= boatLimit and places:
                boatLimit -= people[l]
                places -= 1
                l += 1
            res += 1
        
        return res