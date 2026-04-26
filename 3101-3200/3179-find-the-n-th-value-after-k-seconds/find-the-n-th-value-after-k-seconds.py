class Solution:
    # Pascal Triangle
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return factorial(k + n - 1)//(factorial(k) * factorial(n-1)) % 1_000_000_007