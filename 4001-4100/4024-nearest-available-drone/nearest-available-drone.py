class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        res, bestDist = -1, math.inf
        for i, (x, y, r) in enumerate(drones):
            curDist = abs(x - target[0]) + abs(y - target[1])
            if curDist <= r and curDist < bestDist:
                res, bestDist = i, curDist
        
        return res
