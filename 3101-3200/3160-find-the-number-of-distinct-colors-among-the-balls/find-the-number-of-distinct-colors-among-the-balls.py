class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [None] * len(queries)
        ballColors = defaultdict(int)
        colorCnt = defaultdict(int)

        for i, (ball, color) in enumerate(queries):
            if curBallCollor := ballColors[ball]:
                colorCnt[curBallCollor] -= 1
                if colorCnt[curBallCollor] == 0:
                    del colorCnt[curBallCollor]
            
            ballColors[ball] = color
            colorCnt[color] += 1
            res[i] = len(colorCnt)

        return res
