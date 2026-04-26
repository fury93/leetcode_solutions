class Solution:
    def minTotalDistance(self, grid):
        row_sum = list(map(sum, grid))
        col_sum = list(map(sum, zip(*grid)))

        def minTotalDistance1D(vec):
            i, j = -1, len(vec)
            d = left = right = 0
            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            return d

        return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)
        