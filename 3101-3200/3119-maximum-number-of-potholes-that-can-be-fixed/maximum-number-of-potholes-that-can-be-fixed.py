class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        groups = [len(x) for x in road.split(".")if x]
        groups.sort(reverse = True) 
        total_fixed = 0    
        remaning_budget = budget
    
        for size in groups:
            cost = size + 1 
            if remaning_budget >= cost:
                total_fixed += size
                remaning_budget -= cost
            else:
                if remaning_budget > 1:  
                    total_fixed += remaning_budget - 1 
                break

        return total_fixed
        

class Solution2:
    def maxPotholes(self, road: str, budget: int) -> int:
        res = 0
        for holes in sorted(map(len, road.split('.')), reverse=True):
            res += min(holes, max(0, budget - 1))
            budget -= min(holes + 1, budget)
        return res