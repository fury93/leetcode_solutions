class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def getTimes(starts):
            times = [[None] * cols for _ in range(rows)]
            q = deque()
            for r, c in starts:
                times[r][c] = 0
                q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and times[nr][nc] is None and grid[nr][nc] == 0:
                        times[nr][nc] = times[r][c] + 1
                        q.append((nr, nc))
            return times

        fireStarts = [(r, c) for r, c in product(range(rows), range(cols)) if grid[r][c] == 1]
        peopleStarts = [(0, 0)]

        fireTimes = getTimes(fireStarts)
        peopleTimes = getTimes(peopleStarts)

        peopleFinalTime = peopleTimes[-1][-1]
        fireFinalTime = fireTimes[-1][-1]

        if peopleFinalTime is None:
            return -1
        if fireFinalTime is None:
            return 10**9

        finalDiff = fireFinalTime - peopleFinalTime
        if finalDiff < 0:
            return -1

        def getFireAndPeopleTimeDiff(r, c):
            if peopleTimes[r][c] is None:
                return -1
            if fireTimes[r][c] is None:
                return peopleTimes[r][c]
            return fireTimes[r][c] - peopleTimes[r][c]

        #edge-case when people and fire can go to the final at the same time (only when different paths)
        topDiff = getFireAndPeopleTimeDiff(-2, -1)
        leftDiff = getFireAndPeopleTimeDiff(-1, -2)

        if topDiff > finalDiff or leftDiff > finalDiff:
            return finalDiff
        
        return finalDiff - 1 # not if diff is 0 will return -1, it's correct