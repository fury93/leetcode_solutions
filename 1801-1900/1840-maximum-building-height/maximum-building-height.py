class Solution:
    def maxBuilding(self, n: int, re: List[List[int]]) -> int:
        re.sort(key=lambda i:i[0]+i[1])
        ans, b = 0, [1,0]
        for r in re:
            ans = max(ans,(min(2*n-b[0]+b[1],r[0]+r[1])-(b[0]-b[1]))//2)
            if b[0]-b[1] < r[0]-r[1]: b = [r[0],r[1]]
        return max(ans,n-b[0]+b[1])
        
class Solution2:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions
        # Add restriction (1, 0)
        r.append([1, 0])
        r.sort()

        # Add restriction (n, n-1)
        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)

        # Pass restrictions from left to right
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        # Pass restrictions from right to left
        for i in range(m - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        ans = 0
        for i in range(m - 1):
            # Calculate the maximum height of the buildings between r[i][0] and r[i][1]
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            ans = max(ans, best)

        return ans