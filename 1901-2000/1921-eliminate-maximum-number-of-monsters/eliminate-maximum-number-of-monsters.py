class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivalTime = sorted(d / s for d, s in zip(dist, speed))
        res = 0
        for shot, arrival in enumerate(arrivalTime):
            if shot >= arrival: break
            res += 1
        return res
