class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        l, r = min(buckets), sum(buckets) / len(buckets) # initialize lowest and highest possible value
        left_over = 1-loss/100                           # calculate left over ratio
        def ok(val):                                     # check if reach to an average of `val` is posible
            cnt = 0
            for bucket in buckets:
                if bucket >= val:
                    cnt += (bucket - val) * left_over    # count left_over after pouring water
                else:
                    cnt -= (val - bucket)                # reduce count for those bucket need more water to reach `val`
            return cnt >= 0
        while r - l >= 1e-5:                             # by description, epsilon is 1e-5
            mid = (l + r) / 2                            # binary search
            if ok(mid):
                l = mid 
            else:    
                r = mid 
        return r