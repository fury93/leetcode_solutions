class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        prefix = [False] * len(nums)
        pq = []
        for i, x in enumerate(nums): 
            if len(pq) == k and -pq[0] < x: prefix[i] = True
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        ans = 0 
        pq = []
        for i, x in reversed(list(enumerate(nums))): 
            if len(pq) == k and -pq[0] < x and prefix[i]: ans += 1
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        return ans 