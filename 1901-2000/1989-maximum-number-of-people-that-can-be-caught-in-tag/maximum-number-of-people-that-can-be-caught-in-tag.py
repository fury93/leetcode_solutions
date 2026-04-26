class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        ans = j = 0
        n = len(team)
        for i, x in enumerate(team):
            if x:
                while j < n and (team[j] or i - j > dist):
                    j += 1
                if j < n and abs(i - j) <= dist:
                    ans += 1
                    j += 1
        return ans
        
class Solution2:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        not_it = it = ans = 0
        for _, is_it in enumerate(team):
            if is_it:                   # if is `it`
                if not_it > 0:          #     if there are some non-caught `not_it`, try catch it
                    not_it -= 1
                    ans += 1            #     and count people caught
                else:
                    it += 1             #     if there are no non-caught `not_it`, increase count of `it`
            else:                       # it not `it`
                if it > 0:              #     if there are enough "catch quota" leftover, use them (catch `not_it` before previous index)
                    it -= 1 
                    ans += 1            #     decrease count of `it` and count people caught
                else:                   
                    not_it += 1         #     if there are no quota to catch `not_it`, increase count of `not_it`
            not_it = min(not_it, dist)  # eliminate outdated `not_it` by limiting its count under `dist`
            it = min(it, dist)          # eliminate outdated `it` by limiting its count under `dist`
        return ans