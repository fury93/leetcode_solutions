class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        minVal = min(cnt.keys())
        if minVal < k:
            return -1
        elif minVal == k:
            return len(cnt) - 1
        
        return len(cnt)