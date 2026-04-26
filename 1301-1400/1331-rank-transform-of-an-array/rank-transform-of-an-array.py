class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for val in sorted(arr):
            rank.setdefault(val, len(rank) + 1)
        
        return list(map(rank.get, arr))