class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        ans = 0
        neighbors = defaultdict(set)
        for firstNode, thirdNode in corridors:
            neighbors[thirdNode].add(firstNode)
            neighbors[firstNode].add(thirdNode)
            ans += len(neighbors[firstNode].intersection(neighbors[thirdNode]))
        return ans