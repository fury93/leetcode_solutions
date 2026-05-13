class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        deltas = [0] * ((limit << 1) + 2)

        lp = 0
        rp = n - 1
        while lp < rp:
            left, right = nums[lp], nums[rp]
            if left <= right:
                small, large = left, right
            else:
                small, large = right, left
            
            deltas[small + 1] -= 1
            deltas[small + large] -= 1
            deltas[small + large + 1] += 1
            deltas[large + limit + 1] += 1

            lp += 1
            rp -= 1
        return n + min(accumulate(deltas))
        
class Solution2:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sum_count = Counter()
        min_arr = []
        max_arr = []

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            sum_count[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)

        min_arr.sort()
        max_arr.sort()

        min_ops = n

        for c in range(2, 2 * limit + 1):
            add_left = n // 2 - bisect_left(min_arr, c)
            add_right = bisect_left(max_arr, c - limit)

            current_ops = n // 2 + add_left + add_right - sum_count[c]
            min_ops = min(min_ops, current_ops)

        return min_ops