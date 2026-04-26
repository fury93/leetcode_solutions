class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        _, leaveCounts = zip(*Counter(s).most_common(k))
        return len(s) - sum(leaveCounts)