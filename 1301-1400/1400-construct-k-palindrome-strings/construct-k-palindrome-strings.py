class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        cnt = Counter(s)
        odd = sum(val & 1 for val in cnt.values())
        return odd <= k
