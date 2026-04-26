class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        return max(a + b for a, b in zip(sorted(processorTime), sorted(tasks, reverse=True)[::4]))