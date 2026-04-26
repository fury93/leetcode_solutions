class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCount = Counter(tasks).values()
        return -1 if 1 in taskCount else sum((cnt+2)//3 for cnt in taskCount)