class Solution:
    def numOfWays(self, n: int) -> int:
        """
        12 ways in first row:
        - 6 ways using 2-colors, each for which the next row has:
            - 3 ways using 2-colors
            - 2 ways using 3-colors
        - 6 ways using 3-colors, each for which the next row has:
            - 2 ways using 2-colors
            - 2 ways using 3-colors
        """
        mod = 10**9 + 7

        count2 = count3 = 6
        for _ in range(n - 1):
            prev2, prev3 = count2, count3
            count2 = 3 * prev2 + 2 * prev3
            count3 = 2 * prev2 + 2 * prev3
        
        return (count2 + count3) % mod