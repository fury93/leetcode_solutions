class Solution2:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        res, x, y, dx, dy  = 0, 0, 0, 0, 1

        for command in commands:
            match command:
                case -1: dx, dy = dy, -dx # clockwise
                case -2: dx, dy = -dy, dx # anti-clockwise
                case steps:
                    for _ in range(steps):
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in obstacles: break
                        x, y = nx, ny

                    res = max(res, x**2 + y**2)

        return res

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        res, x, y, i = 0, 0, 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # north, east, south, west

        for command in commands:
            match command:
                case -1: i = (i+1) % 4
                case -2: i = (i-1) % 4
                case steps:
                    dx, dy = direction[i]
                    for _ in range(steps):
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in obstacles: break
                        x, y = nx, ny

                    res = max(res, x**2 + y**2)

        return res
