class Solution:
    def generatePossibleNextMoves(self, states: str) -> List[str]:
        res = []
        for i in range(1, len(states)):
            if states[i] == states[i-1] == '+':
                res.append(states[:i-1] + '--' + states[i+1:])
        return res