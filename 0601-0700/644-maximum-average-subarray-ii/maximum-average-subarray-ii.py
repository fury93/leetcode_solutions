class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        points= [[0,0]]
        for num in nums:
            points.append([len(points), points[-1][1] + num])
        def get_slope(i, j):
            return (points[i][1]-points[j][1]) / (points[i][0]-points[j][0])
        hull = collections.deque()
        ans = float('-inf')
        for j in range(k, len(points)):
            while len(hull) >= 2 and get_slope(hull[-2], hull[-1]) >= get_slope(hull[-1], j-k):
                hull.pop()
            hull.append(j-k)
            
            while len(hull) >= 2 and get_slope(hull[0], hull[1]) <= get_slope(hull[0], j):
                hull.popleft()
            ans = max(ans, get_slope(hull[0],j))
        return ans