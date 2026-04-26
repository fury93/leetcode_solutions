class Solution:
    def minNumberOfSeconds(self, H: int, arr: List[int]) -> int:
        S = sum(arr)
        N = len(arr)
        V = ceil(H / N)
        start, end = 1, V * (V + 1) * max(arr) // 2
        while start < end:
            mid = (start + end) // 2
            W = 0
            for T in arr:
                W += floor(sqrt(2 * mid / T + 0.25) - 0.5)
            if W >= H:
                end = mid
            else:
                start = mid + 1
        return start
        
class Solution2:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r = 1, maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2
        eps = 1e-7
        res = 0

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res