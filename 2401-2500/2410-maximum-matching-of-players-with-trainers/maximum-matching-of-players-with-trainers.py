class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        res, i = 0, 0
        for t in trainers:
            if players[i] <= t:
                res += 1
                i += 1
            if i == len(players): break
            

        return res