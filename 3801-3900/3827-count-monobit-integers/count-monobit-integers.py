class Solution:
    def countMonobit(self, n: int) -> int:
        return (n + 1).bit_length()