class Solution:
    def countLargestGroup(self, n: int) -> int:
        return len(multimode(sum(map(int, str(i))) for i in range(1, n+1)))