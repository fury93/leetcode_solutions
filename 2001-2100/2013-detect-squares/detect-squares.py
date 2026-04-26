class DetectSquares:
    def __init__(self):
        self.yPoints = defaultdict(list)
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.yPoints[y].append(x)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res, (x1, y1) = 0, point
        for x2 in self.yPoints[y1]:
            if x1 == x2: continue
            side = abs(x2 - x1)

            yBottom = y1 - side
            res += self.cnt[(x1, yBottom)] * self.cnt[(x2, yBottom)]
            yUp = y1 + side
            res += self.cnt[(x1, yUp)] * self.cnt[(x2, yUp)]
        return res