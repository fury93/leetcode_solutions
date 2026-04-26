class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        return max((j+w-1)//w for j, w in zip(sorted(jobs), sorted(workers)))