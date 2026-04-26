class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        m, n = len(land), len(land[0])
        flood = collections.deque()
        move = collections.deque()
        for i in range(m):
            for j in range(n):
                if land[i][j] == "S": move.append((i, j))
                if land[i][j] == "*": flood.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        secs = 0
        while move:
            l1, l2 = len(flood), len(move)
            for _ in range(l1):
                x, y = flood.popleft()
                for dx, dy in dirs:
                    cx, cy = x + dx, y + dy
                    if 0 <= cx < m and 0 <= cy < n and land[cx][cy] == ".":
                        land[cx][cy] = "*"
                        flood.append((cx, cy))

            for _ in range(l2):
                x, y = move.popleft()
                if land[x][y] == "D": return secs
                for dx, dy in dirs:
                    cx, cy = x + dx, y + dy
                    if 0 <= cx < m and 0 <= cy < n and (land[cx][cy] == "." or land[cx][cy] == "D"):
                        if land[cx][cy] != "D": land[cx][cy] = "*"
                        move.append((cx, cy))
            secs += 1
        
        return -1