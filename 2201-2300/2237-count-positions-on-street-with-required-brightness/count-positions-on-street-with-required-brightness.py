class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        brightness = [0] * (n + 1)
        for position, radius in lights:
            left = max(0, position - radius)
            right = min(n-1, position + radius)
            brightness[left] += 1
            brightness[right + 1] -= 1
        
        return sum(have >= need for have, need 
            in zip(accumulate(brightness), requirement))