class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda: [0, 0]) # (diffHeight, diffCnt)
        for start, end, height in buildings:
            d[start][0] += height
            d[start][1] += 1
            d[end][0] -= height
            d[end][1] -= 1

        res, segmentHeight, segmentCnt, d = [], 0, 0, sorted(d.items())
        for i in range(len(d)-1):
            start, end, diffHeight, diffCnt = d[i][0], d[i+1][0], d[i][1][0], d[i][1][1]
            segmentHeight += diffHeight
            segmentCnt += diffCnt
            if segmentCnt > 0:
                averageHeight = segmentHeight//segmentCnt
                # merge with previous segment if they have the same average height and is neighbours
                if res and res[-1][1] == start and res[-1][2] == averageHeight:
                    res[-1][1] = end
                else:
                    res.append([start, end, averageHeight])
        return res