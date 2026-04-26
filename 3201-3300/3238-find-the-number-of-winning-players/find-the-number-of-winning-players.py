class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        picks = [[0] * 11 for _ in range(n)]

        for player, color in pick:
            picks[player][color] += 1

        return sum(i < max(picks[i]) for i in range(n))