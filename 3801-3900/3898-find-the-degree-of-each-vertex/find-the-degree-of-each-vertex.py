class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(edges) for edges in zip(*matrix)]