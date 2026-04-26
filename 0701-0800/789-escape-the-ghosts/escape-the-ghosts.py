class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Manhattan distance
        def getDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        escapeDist = getDistance([0, 0], target)

        return all(escapeDist < getDistance(ghost, target) for ghost in ghosts)