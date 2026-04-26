class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        total = sum(calories[:k])
        if total < lower:
            score -= 1
        if total > upper:
            score += 1
        
        for right in range(k, len(calories)):
            total = total + calories[right] - calories[right - k]
            if total < lower:
                score -= 1
            if total > upper:
                score += 1
        
        return score
        
            
        
class Solution2:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res, sm, k = 0, 0, k - 1
        for r, cal in enumerate(calories):
            sm += cal
            l = r - k
            if l < 0: continue
            res -= sm < lower
            res += sm > upper
            sm -= calories[l]

        return res