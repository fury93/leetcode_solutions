class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        n = len(s)
        count = collections.Counter(s)
        max_val = max(count.values())
        max_count = sum(1 for val in count.values() if val == max_val)
        if (max_val-1)*k+max_count > n:
            return ""
        
        buckets = [[] for _ in range(max_val)]
        cnt = 0
        for key in sorted(count, key = lambda x: -count[x]):
            divisor = max_val if count[key] == max_val else max_val-1
            for _ in range(count[key]):
                buckets[cnt% divisor].append(key)
                cnt += 1
        return "".join(["".join(bucket) for bucket in buckets])